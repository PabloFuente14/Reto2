from django.contrib import admin
from .models import Categoria, Componente, Producto ,LineaPedido, Cliente ,Pedido
# Register your models here.

admin.site.register([Categoria, Componente, Producto ,LineaPedido, Cliente ,Pedido])