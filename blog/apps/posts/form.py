from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200, help_text="Required")
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    icono = forms.ImageField(label="imagen de perfil", required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "icono",
        ]
