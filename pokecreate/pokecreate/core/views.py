from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.decorators.http import require_GET
from .models import Pokemon
# Create your views here.


def index(request):
    return render(request,'index.html')

def pokemons(request):
    search = request.GET.get('search')

    pokemons = Pokemon.objects.all()

    if search:
        pokemons = pokemons.filter(nome__icontains=search)
        
    ctx = {
        'pokemons': pokemons
    }
    return render(request, 'core/pokemons.html', ctx)


def sobre(request):
    return render(request, 'core/sobre.html')
