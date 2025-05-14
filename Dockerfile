FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONUNBUFFERED=1 DJANGO_SETTINGS_MODULE=text_generator.settings

RUN python manage.py collectstatic --noinput && python manage.py migrate --noinput

CMD ["gunicorn", "text_generator.wsgi:application", "--bind", "0.0.0.0:8000"]
