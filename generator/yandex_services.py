import os
import time
import logging

import requests
from requests.exceptions import RequestException
from dotenv import load_dotenv

load_dotenv()

GPT_ID = os.getenv('YANDEX_GPT_ID')
API_KEY = os.getenv('YANDEX_API_KEY')
MAX_TOKENS = 200

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

"""
Функция для генерации текста с использованием Yandex GPT.
Получает тему, язык и длину текста в качестве параметров.
Возвращает сгенерированный текст или пустую строку в случае ошибки.
"""
def generate_text(
    topic: str,
    language: str = 'ru',
    length: int = 120,
    retries: int = 3,
    backoff: float = 1.0
) -> str:

    if not GPT_ID or not API_KEY:
        logger.error("YANDEX_GPT_ID или YANDEX_API_KEY не заданы в .env")
        return ""

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type":  "application/json",
        "Authorization": f"Api-Key {API_KEY}",
    }
    body = {
        "modelUri": f"gpt://{GPT_ID}/yandexgpt-lite/latest",
        "completionOptions": {
            "stream":            False,
            "temperature":       0.9,
            "topP":              0.95,
            "repetitionPenalty": 1.2,
            "maxTokens":         str(MAX_TOKENS),
        },
        "messages": [
            {
                "role": "system",
                "text": (
                    "Ты ассистент для генерации чистых синтетических "
                    "текстовых данных для обучения моделей искусственного интеллекта. "
                    "Не используй приветствия, обращения к читателю, слова «Привет» и их аналоги. "
                    "Пиши только связный, фактический текст по заданной теме."
                )
            },
            {
                "role": "user",
                "text": (
                    f"Сгенерируй текст на тему «{topic}» длиной примерно {length} слов "
                    f"на языке {language.upper()}, без вводных фраз и обращений; "
                    "концентрируйся на описании фактов и понятий, пригодных для тренировки ИИ."
                )
            },
        ]
    }


    for attempt in range(1, retries + 1):
        try:
            resp = requests.post(url, headers=headers, json=body, timeout=30)
            resp.raise_for_status()

            data = resp.json()
            alt_list = data.get('result', {}).get('alternatives', [])
            if not alt_list:
                raise KeyError("пустой список 'alternatives' в ответе")

            message = alt_list[0].get('message', {})
            text = message.get('text', '').strip()
            if not text:
                raise ValueError("поле 'text' пустое")
            return text

        except RequestException as e:
            logger.warning(f"[YandexGPT] Сетевой сбой (попытка {attempt}): {e}")
        except ValueError as e:
            logger.warning(f"[YandexGPT] Пустой текст или JSON: {e}")
        except KeyError as e:
            logger.warning(f"[YandexGPT] Структура ответа сломана: {e}")
        except Exception as e:
            logger.exception(f"[YandexGPT] Неожиданная ошибка: {e}")

        if attempt < retries:
            time.sleep(backoff * (2 ** (attempt - 1)))

    logger.error(f"[YandexGPT] Не удалось получить ответ после {retries} попыток.")
    return ""
