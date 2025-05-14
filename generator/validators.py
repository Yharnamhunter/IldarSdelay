from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MinimumLengthValidator:
    """
    Проверяет, что пароль имеет минимальную длину.
    """
    def __init__(self, min_length=6):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("Пароль должен содержать не менее %(min_length)d символов."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _("Ваш пароль должен содержать не менее %(min_length)d символов.") % {
            'min_length': self.min_length
        }


class UppercaseValidator:
    """
    Проверяет, что пароль содержит хотя бы одну заглавную букву.
    """
    def validate(self, password, user=None):
        if not any(c.isupper() for c in password):
            raise ValidationError(
                _("Пароль должен содержать хотя бы одну заглавную букву."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _("Ваш пароль должен содержать хотя бы одну заглавную букву (A–Z).")


class NumericValidator:
    """
    Проверяет, что пароль содержит хотя бы одну цифру.
    """
    def validate(self, password, user=None):
        if not any(c.isdigit() for c in password):
            raise ValidationError(
                _("Пароль должен содержать хотя бы одну цифру."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _("Ваш пароль должен содержать хотя бы одну цифру (0–9).")


class SpecialCharacterValidator:
    """
    Проверяет, что пароль содержит хотя бы один специальный символ.
    """
    def __init__(self, special_characters="!@#$%^&*()_+-={}[]:\";'<>?,./"):
        self.special_characters = set(special_characters)

    def validate(self, password, user=None):
        if not any(c in self.special_characters for c in password):
            raise ValidationError(
                _("Пароль должен содержать хотя бы один специальный символ: %(chars)s"),
                code='password_no_special',
                params={'chars': ''.join(self.special_characters)},
            )

    def get_help_text(self):
        return _("Ваш пароль должен содержать хотя бы один из специальных символов: %(chars)s") % {
            'chars': ''.join(self.special_characters)
        }
