from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrarForm(UserCreationForm):
    email = forms.EmailField()
    nome = forms.CharField(max_lenght=100)

    clas Meta:
    model = User
    fields = ['username', 'nome', 'email', 'password1', 'password2']