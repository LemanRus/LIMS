from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.utils.datetime_safe import datetime

from .models import CustomUser

class PasswordResetValidateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('secret_answer', 'password')
        labels = {
            'secret_answer': 'Ответ',
            'password': 'Введите новый пароль',
        }
