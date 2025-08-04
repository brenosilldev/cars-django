from django.shortcuts import render
from carros.models import Carro


# Create your views here.

# Função para renderizar o template

def carro_view(request):
    # Tras todos os dados dvor 
    carros = Carro.objects.all()    
    print(carros)
    
    return render(request, 'carros.html',{
        'carros': carros
    })  