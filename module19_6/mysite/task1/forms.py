from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label="Введите логин")
    password = forms.CharField(min_length=8, label="Введите пароль")
    repeat_password = forms.CharField(min_length=8, label="Повторите пароль")
    age = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)], label="Введите свой возраст")