from django.urls import path
from . import views

"""
URL-маршруты приложения 
- генерацию одиночных текстов,
- пакетную генерацию и потоковую передачу,
- скачивание готового файла,
- очистку истории
"""

urlpatterns = [
    path('', views.generate_view, name='generate'),
    path('batch/', views.batch_generate_view, name='batch_generate'),
    path('batch/stream/', views.batch_stream, name='batch_stream'),
    path('batch/download/<str:filename>', views.batch_download_view, name='batch_download'),
    path('generate/clear/', views.clear_text_history,  name='clear_text_history'),
    path('batch/clear/', views.clear_batch_history, name='clear_batch_history'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
