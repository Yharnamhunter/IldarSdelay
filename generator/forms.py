from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """
    Форма регистрации нового пользователя.
    Поля:
    - username: имя пользователя.
    - email:    электронная почта.
    - password1: пароль.
    - password2: подтверждение пароля.
    """
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
        }

class LoginForm(AuthenticationForm):
    """
    Форма авторизации пользователя.
    Поля:
    - имя пользователя.
    - пароль.
    """
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )
