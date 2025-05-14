from django.core.exceptions import ValidationError
import re

def validate_contains_digit(value):
    if not re.search(r'\d', value):
        raise ValidationError('Пароль должен содержать хотя бы одну цифру.')

def validate_contains_upper(value):
    if not re.search(r'[A-ZА-Я]', value):
        raise ValidationError('Пароль должен содержать заглавную букву.')

def validate_no_username(value, user=None):
    if user and user.username.lower() in value.lower():
        raise ValidationError('Пароль не должен содержать имя пользователя.')
