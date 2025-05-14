from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class textGeneration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField()
    language = models.CharField(max_length=2, choices=[('en','EN'),('ru','RU')])
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class batchGeneration(models.Model):
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
    language    = models.CharField(
        max_length=2, 
        choices=[('en','English'),('ru','Русский')]
    )
    file_format = models.CharField(
        max_length=3,
        choices=[('zip','ZIP'),('csv','CSV'),('txt','TXT')]
    )
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} – {self.created_at:%Y-%m-%d %H:%M}"
