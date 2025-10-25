# core/forms.py
from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=75, label='Nome')
    email = forms.EmailField(label='e-mail')
    assunto = forms.CharField(max_length=200, label='Assunto')
    conteudo = forms.CharField(widget=forms.Textarea, label='Conteúdo')
