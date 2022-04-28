from django.shortcuts import redirect, render
# importamos todas las categorias que necesitamos hacer consulyas a la base de datos
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

#COMPONENTES
    
def componentes(request):
    componentes=Componente.objects.all()
    return render(request, 'componentes/gestion_componentes.html',{'componentes':componentes})

def registrarComponente(request):
    referencia= request.POST["referencia"]
    Componente.objects.create(referencia=referencia)
    return redirect("/componentes")  

    # nombre= request.POST["nombre"]
    # Componente.objects.create(nombre=nombre)
    # return redirect("/componentes")   

    # marca= request.POST["marca"]
    # Componente.objects.create(nombre=nombre)
    # return redirect("/categorias")

                
def ediccionComponente(request,id):
    componente=Componente.objects.get(id=id)
    return render(request,"componentes/ediccion_componente.html", {'componente':componente})

def editarComponente(request):
    id=request.POST["id"]
    nombre= request.POST["nombre"]
    componente= Componente.objects.get(id=id)
    componente.nombre= nombre
    componente.save()
    return redirect("/componentes")

def borrarComponente(request):
    componente=Componente.objects.get(id=id)
    componente.delete()
    return redirect("/componentes")
