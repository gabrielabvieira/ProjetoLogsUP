from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrarForm(UserCreationForm):
    email = forms.EmailField()
    nome = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'nome', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['nome'] 
        if commit:
            user.save()
        return user
