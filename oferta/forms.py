from django import forms
from django.contrib.auth.models import User
from .models import OfertaFormativa

class OfertaForm(forms.ModelForm):
    class Meta:
        model = OfertaFormativa
        fields = ['nome', 'descricao', 'saidas_profissionais', 'carga_horaria', 'disciplinas', 'imagem']

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
