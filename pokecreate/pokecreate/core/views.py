from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
# Create your views here.


def index(request):
    return render(request,'index.html')

def pokemons(request):
    pokemons= Pokemon.objects.all()
    ctx = {
        'pokemons': pokemons
    }
    return render(request, 'core/pokemons.html', context=ctx)

def sobre(request):
    return render(request, 'core/sobre.html')
