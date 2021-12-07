from django.core.checks import messages
from django.shortcuts import render
from core.models import Entregadore, Parceiro
from django.core.mail import send_mail


def home(request):
    model_entregador = Entregadore.objects.all()
    model_parceiro = Parceiro.objects.all()
    
    context = {
        'model_entregador': model_entregador,
        'model_parceiro': model_parceiro
    }
    
    return render(request, 'index.html', context)


def send_email_mrbee(request):
    email = request.POST.get('email')
    name = request.POST.get('name')
    message = request.POST.get('message')
    
    send_mail(
        f'Olá, me chamo {name}, meu email {email}',
        f'{message}',
        'mrbeedeliveryp@gmail.com',
        ['mrbeedeliveryp@gmail.com'],
        fail_silently=False,
    )
    
    return render(request, 'index.html')

