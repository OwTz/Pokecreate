from django.contrib import admin
from .models import *
# Register your models here.


# TODO: classe de views do admi
class viewsAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'data_criacacao', 'data_modificacao']
    search_fields = ['categoria','nome']

#TODO: registro de classes
admin.site.register(Pokemon, viewsAdmin)
