from django.shortcuts import render
from core.models import Entregadore


def home(request):
    model_all_fields = Entregadore.objects.all()
    
    for model2 in model_all_fields:
        print(model2.imagem)
    
    context = {
        'models': model_all_fields 
    }
    
    return render(request, 'index.html', context)



