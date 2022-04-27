from django.shortcuts import redirect, render
from .models import Categoria, Componente, Cliente, Pedido, Producto, LineaPedido 
# Create your views here.

def inicio(request):
    return render(request, 'home/inicio.html')

#CATEGORÍAS

def categorias(request):
    categorias=Categoria.objects.all()
    return render(request, 'categorias/gestion_categorias.html',{'categorias': categorias} )

def registrarCategoria(request):
    nombre= request.POST["nombre"]
    if not Categoria.objects.filter(nombre=nombre).exists():    
        Categoria.objects.create(nombre=nombre)
    return redirect("/categorias")

def ediccionCategoria(request,id):
    categoria=Categoria.objects.get(id=id)
    return render(request,"categorias/ediccion_categoria.html", {'categoria': categoria})

def editarCategoria(request):
    id=request.POST["id"]
    nombre= request.POST["nombre"]
    categoria= Categoria.objects.get(id=id)
    categoria.nombre= nombre
    categoria.save()
    return redirect("/categorias")

def borrarCategoria(request, id):
    categoria=Categoria.objects.get(id=id)
    categoria.delete()
    return redirect("/categorias")
    