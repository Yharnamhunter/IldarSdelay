from django.contrib import admin
from . import models

"""
Регистрируем модели приложения в административной панели Django.
"""

admin.site.register(models.TextGeneration)
admin.site.register(models.BatchGeneration)