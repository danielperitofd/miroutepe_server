from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContatoForm

def construcao(request):
    return render(request, 'em_construcao.html')

def home(request):
    return render(request, 'home.html')

def tecnologia(request):
    return render(request, 'tecnologia.html')

def perguntas(request):
    return render(request, 'perguntas.html')

def parceiros(request):
    return render(request, 'parceiros.html')

def vantagens(request):
    return render(request, 'vantagens.html')

def ailson_team(request):
    return render(request, 'ailson_team.html')

def adjailson_team(request):
    return render(request, 'adjailson_team.html')

def daniel_team(request):
    return render(request, 'daniel_team.html')

def vanthuir_team(request):
    return render(request, 'vanthuir_team.html')

def sobre(request):
    return render(request, 'sobre.html')

def solucoes(request):
    return render(request, 'solucoes.html')

def suporte(request):
    return render(request, 'suporte.html')

def localizacao(request):
    return render(request, 'localizacao.html')

def login_view(request):
    return render(request, 'login.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['conteudo']
            
        # Envia o e-mail

            email_msg = EmailMessage(
            subject=assunto,
            body=mensagem,
            from_email=f"{nome} <{settings.DEFAULT_FROM_EMAIL}>",
            to=['miroutepe@gmail.com'],
            reply_to=[email],
        )
            email_msg.send(fail_silently=False)
            return render(request, 'contato_sucesso.html')  # Redireciona para uma página de sucesso ou confirmação
    else:
        form = ContatoForm()

        return render(request, 'contato.html', {'form': form})

