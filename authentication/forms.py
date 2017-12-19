from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario', 'name': 'username'})
                                )
    password = forms.CharField(label="Contraseña", max_length=30,
                            widget=forms.TextInput(attrs={'class': 'form-control','type':'password','placeholder': 'Contraseña', 'name': 'password'})
                                )
