from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
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

# TODO: pagina sobre o site 
def sobre(request):
    return render(request, 'core/sobre.html')

# TODO: page cadastro de pokemons
def cadastro(request):
    return render(request, 'core/cadastropokemons.html')

# TODO: page for details pokemon with ID
def detalhes(request, id):
    pokemon = get_object_or_404(Pokemon, pk=id)

    ctx = {
        Pokemon : pokemon
    }

    return render(request, 'core/detalhe.html', context=ctx)