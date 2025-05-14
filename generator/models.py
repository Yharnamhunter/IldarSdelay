from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class TextGeneration(models.Model):
    """
    Модель для хранения истории одиночной генерации текста.
    Атрибуты:
    - user: ссылка на пользователя, сделавшего запрос.
    - prompt: текст запроса.
    - result: итог сгенерированного текста.
    - language: язык генерируемого текста.
    - created_at:дата и время создания записи.
    """
    def __str__(self):
        return f"{self.user.username} – {self.created_at:%Y-%m-%d %H:%M}"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField()
    language = models.CharField(
        max_length=2, 
        choices=[('en','EN'),('ru','RU')]
    )
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class BatchGeneration(models.Model):
    """
    Модель для хранения истории пакетной генерации текстов.
    Атрибуты:
    - user: ссылка на пользователя.
    - prompt: общий текст запроса.
    - count: количество сгенерированных текстов.
    - language: язык текстов (ru/en).
    - file_format: формат итогового файла (txt/docx/rtf).
    - created_at: дата и время создания записи.
    """
    def __str__(self):
        return f"{self.user.username} – {self.created_at:%Y-%m-%d %H:%M}"
    user        = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    prompt      = models.TextField(
    )
    count       = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(20)
        ]
    )
    language = models.CharField(
        max_length=2, 
        choices=[('en','EN'),('ru','RU')]
    )
    file_format = models.CharField(
        max_length=4,
        choices=[('docx','DOCX'),('rtf','RTF'),('txt','TXT')]
    )
    created_at  = models.DateTimeField(auto_now_add=True)