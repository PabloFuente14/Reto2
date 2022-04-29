from venv import create
from django.shortcuts import redirect, render
# importamos todas las categorias que necesitamos hacer consulyas a la base de datos
from .models import Categoria, Componente, Cliente, Pedido, Producto, LineaPedido
# Create your views here.


def inicio(request):
    return render(request, 'home/inicio.html')

# CATEGORÍAS


def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/gestion_categorias.html', {'categorias': categorias})


def registrarCategoria(request):
    nombre = request.POST["nombre"]
    if not Categoria.objects.filter(nombre=nombre).exists():
        Categoria.objects.create(nombre=nombre)
    return redirect("/categorias")


def ediccionCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    return render(request, "categorias/ediccion_categoria.html", {'categoria': categoria})


def editarCategoria(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    categoria = Categoria.objects.get(id=id)
    categoria.nombre = nombre
    categoria.save()
    return redirect("/categorias")


def borrarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect("/categorias")

# COMPONENTES


def componentes(request):
    componentes = Componente.objects.all()
    return render(request, 'componentes/gestion_componentes.html', {'componentes': componentes})


def registrarComponente(request):
    referencia = request.POST["referencia"]
    if not Componente.objects.filter(referencia=referencia).exists():
        nombre = request.POST["nombre"]
        marca = request.POST["marca"]
        Componente.objects.create(
            referencia=referencia, nombre=nombre, marca=marca)
    return redirect("/componentes")


def ediccionComponente(request, referencia):
    componente = Componente.objects.get(referencia=referencia)
    return render(request, "componentes/ediccion_componente.html", {'componente': componente})


def editarComponente(request):
    referencia = request.POST["referencia"]
    nombre = request.POST["nombre"]
    marca = request.POST["marca"]
    componente = Componente.objects.get(referencia=referencia)
    componente.nombre = nombre
    componente.marca = marca
    componente.save()
    return redirect("/componentes")


def borrarComponente(request, referencia):
    componente = Componente.objects.get(referencia=referencia)
    componente.delete()
    return redirect("/componentes")

# PRODUCTOS


def productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    componentes = Componente.objects.all()
    return render(request, 'productos/gestion_productos.html', {'productos': productos, 'categorias': categorias, 'componentes': componentes})


def registrarProducto(request):
    referencia = request.POST["referencia"]
    if not Producto.objects.filter(referencia=referencia).exists():
        nombre = request.POST["nombre"]
        precio = request.POST["precio"]
        descripcion = request.POST["descripcion"]
        id_categoria = request.POST["categorias"]
        categoria = Categoria.objects.get(id=id_categoria)
        referencias_componentes = request.POST.getlist("componentes")
        producto = Producto.objects.create(
            referencia=referencia, nombre=nombre, precio=precio, descripcion=descripcion, categoria=categoria)
        for referencia in referencias_componentes:
            componente = Componente.objects.get(referencia=referencia)
            producto.componentes.add(componente)
    return redirect("/productos")

# def ediccionProducto(request,referencia):
#     producto=Producto.objects.get(referencia=referencia)
#     categorias=Categoria.objects.all()
#     componentes=Componente.objects.all()
#     # return render(request,"productos/ediccion_producto.html", {'producto':producto,'categorias':categorias,'componentes':componentes })






    # CLIENTES
    
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/gestion_clientes.html', {'clientes': clientes})


def registrarCliente(request):

    cif = request.POST["cif"]
    if not Cliente.objects.filter(cif=cif).exists():
        nombre = request.POST["nombre"]
        direccion = request.POST["direccion"]
        ciudad = request.POST["ciudad"]
        telefono = request.POST["telefono"]
        #correo = request.POST["correo"] ///añadir correo=correo
        Cliente.objects.create(cif=cif, nombre=nombre, direccion=direccion,
                               ciudad=ciudad, telefono=telefono)
    return redirect("/clientes")



def ediccionCliente(request, cif):
    cliente= Cliente.objects.get(cif=cif)
    return render(request, "clientes/ediccion_clientes.html", {'cliente': cliente})


def editarCliente(request):
    cif= request.POST["cif"]
    nombre = request.POST["nombre"]
    direccion = request.POST["direccion"]
    cuidad = request.POST["cuidad"]
    telefono = request.POST["telefono"]
    # correo = request.POST["correo"]
    cliente = Cliente.objects.get(cif=cif)
    cliente.nombre = nombre
    cliente.direccion = direccion
    cliente.cuidad = cuidad
    cliente.telefono = telefono
    # cliente.correo = correo
    cliente.save()
    return redirect("/clientes")

def borrarCliente(request, cif):
    cliente = Cliente.objects.get(cif=cif)
    cliente.delete()
    return redirect("/clientes")
