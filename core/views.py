from django.shortcuts import render
from .models import Entregadore, Parceiro
from django.views.generic import (
    CreateView
)
from django.urls import reverse_lazy


def home(request):
    model_entregador = Entregadore.objects.all()
    model_parceiro = Parceiro.objects.all()
    
    context = {
        'entregadores': model_entregador,
        'parceiros': model_parceiro
    }
    
    return render(request, 'index.html', context)


class CrieteViewEntregador(CreateView):
    template_name = 'create_entregador.html'
    model = Entregadore
    
    fields = [
        'nome',
        'endereco',
        'telefone',
        'imagem',
        'cnh',
        'doc_moto',
    ]
    
    success_url = reverse_lazy('home')


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
