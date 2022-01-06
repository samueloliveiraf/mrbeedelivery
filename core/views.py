from django.shortcuts import render
from .models import Entregadore, Parceiro
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import time


def home(request):
    model_entregador = Entregadore.objects.all()
    model_parceiro = Parceiro.objects.all()
    
    context = {
        'entregadores': model_entregador,
        'parceiros': model_parceiro
    }
    
    return render(request, 'index.html', context)


# def send_email_mrbee(request):
#     email = request.POST.get('email')
#     name = request.POST.get('name')
#     message = request.POST.get('message')
#     number = request.POST.get('number')
#     cnh = request.POST.get('cnh')
#     doc = request.POST.get('doc')
    
#     send_mail(
#         f'Olá, me chamo {name}',
#         f'{message}, meu número {number}, meu e-mail {email}{cnh}{doc}',
#         'mrbeedeliveryp@gmail.com',
#         ['mrbeedeliveryp@gmail.com'],
#         fail_silently=False,
#     )
    
#     time.sleep(3)
    
#     return HttpResponseRedirect("/")
