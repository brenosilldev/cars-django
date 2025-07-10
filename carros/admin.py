from django.contrib import admin
from carros.models import Carro as Card
from carros.models import Marca

# Register your models here.

class Carro(admin.ModelAdmin):
    list_display = ( 'modelo', 'ano', 'cor','anofabricacao','anofabricacao','idmarca')
    search_fields = ('modelo',)


class CarroMarca(admin.ModelAdmin):
    list_display = ('marca',)
    search_fields = ('marca',)



# Registro de tabelas para usar
admin.site.register(Card, Carro)
admin.site.register(Marca, CarroMarca)