from math import prod
from tkinter import image_names
from venv import create
from django.core.paginator import Paginator
from django.db.models import Q
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
    productos = None
    texto_busqueda = request.POST.get("texto_busqueda", "")
    if texto_busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains=texto_busqueda) |
            Q(descripcion__icontains=texto_busqueda) |
            Q(referencia__icontains=texto_busqueda) |
            Q(precio__icontains=texto_busqueda) |
            Q(categoria__nombre__icontains=texto_busqueda)|
            Q(componentes__nombre__icontains = texto_busqueda) 
        )
    else:
        productos = Producto.objects.all()

    cantidad_por_pagina = 5
    # E3 - Paginador de productos, con 5 de maximo
    paginator = Paginator(productos, cantidad_por_pagina)
    # Obtenemos el número de página que queremos
    pagina = request.GET.get("page", 1)
    # Obtenemos los productos de esa pagina
    productos = paginator.get_page(pagina)
    pagina_actual = int(pagina)  # Página actual
    paginas = range(1, productos.paginator.num_pages + 1)  # Total de páginas

    categorias = Categoria.objects.all()
    componentes = Componente.objects.all()
    return render(request, 'productos/gestion_productos.html', {
        'productos': productos,
        'categorias': categorias,
        'componentes': componentes,
        'texto_consulta': texto_busqueda,
        'cantidad_por_pagina': cantidad_por_pagina,
        'pagina_actual': pagina_actual,
        'num_paginas': paginas
    })


def registrarProducto(request):
    referencia = request.POST["referencia"]
    if not Producto.objects.filter(referencia=referencia).exists():
        nombre = request.POST["nombre"]
        precio = request.POST["precio"]
        descripcion = request.POST["descripcion"]
        id_categoria = request.POST["categorias"]
        categoria = Categoria.objects.get(id=id_categoria)
        referencias_componentes = request.POST.getlist("componentes")
        imagen=request.FILES.GET('imagen')   # Añadido entrega3, type imagen-->guarda la imagen
        producto = Producto.objects.create(
            referencia=referencia, nombre=nombre, precio=precio, descripcion=descripcion, categoria=categoria, imagen=imagen)
        for referencia in referencias_componentes:
            componente = Componente.objects.get(referencia=referencia)
            producto.componentes.add(componente)
    return redirect("/productos")


def ediccionProducto(request, referencia):
    producto = Producto.objects.get(referencia=referencia)
    categorias = Categoria.objects.all()
    componentes = Componente.objects.all()

    componentes_calculados = []

    for comp in componentes:
        componente_es_usado_en_producto = False
        for pcomp in producto.componentes.all():
            if pcomp.referencia == comp.referencia:
                componente_es_usado_en_producto = True

        # Esta tupla tiene en el indice 0 el componente y en el indice 1 un booleano que indica si el compoente pertence al producto
        tupla = (comp, componente_es_usado_en_producto)
        componentes_calculados.append(tupla)

    print(componentes_calculados)
    return render(request, "productos/ediccion_producto.html", {'producto': producto, 'categorias': categorias, 'componentes_formato_tupla': componentes_calculados})


def editarProducto(request):
    referencia = request.POST["referencia"]
    nombre = request.POST["nombre"]
    precio = float(request.POST["precio"].replace(",", "."))
    descripcion = request.POST["descripcion"]
    id_categoria = request.POST["categorias"]
    categoria = Categoria.objects.get(id=id_categoria)
    referencias_componentes = request.POST.getlist("componentes")
    producto = Producto.objects.get(referencia=referencia)
    producto.nombre = nombre
    producto.precio = precio
    producto.descripcion = descripcion
    producto.categoria = categoria
    for componente in producto.componentes.all():
        producto.componentes.remove(componente)
    for referencia in referencias_componentes:
        componente = Componente.objects.get(referencia=referencia)
        producto.componentes.add(componente)
    producto.save()
    return redirect("/productos")


def borrarProducto(request, referencia):
    producto = Producto.objects.get(referencia=referencia)
    producto.delete()
    return redirect("/productos")

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
        correo = request.POST["correo"]
        Cliente.objects.create(cif=cif, nombre=nombre, direccion=direccion,
                               ciudad=ciudad, telefono=telefono, correo=correo)
    return redirect("/clientes")


def ediccionCliente(request, cif):
    cliente = Cliente.objects.get(cif=cif)
    return render(request, "clientes/ediccion_clientes.html", {'cliente': cliente})


def editarCliente(request):
    cif = request.POST["cif"]
    nombre = request.POST["nombre"]
    direccion = request.POST["direccion"]
    ciudad = request.POST["ciudad"]
    telefono = request.POST["telefono"]
    correo = request.POST["correo"]
    cliente = Cliente.objects.get(cif=cif)
    cliente.nombre = nombre
    cliente.direccion = direccion
    cliente.ciudad = ciudad
    cliente.telefono = telefono
    cliente.correo = correo
    cliente.save()
    return redirect("/clientes")


def borrarCliente(request, cif):
    cliente = Cliente.objects.get(cif=cif)
    cliente.delete()
    return redirect("/clientes")

    # PEDIDOS


def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/gestion_pedidos.html', {'pedidos': pedidos})


def nuevoPedido(request):
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'pedidos/nuevo_pedido.html', {'clientes': clientes, 'productos': productos})


def registrarPedido(request):
    referencia = request.POST["referencia"]
    if not Pedido.objects.filter(referencia=referencia).exists():
        fecha = request.POST["fecha"]
        cif_cliente = request.POST["clientes"]
        cliente = Cliente.objects.get(cif=cif_cliente)
        precio_total = 0
        pedido = Pedido.objects.create(
            referencia=referencia, fecha=fecha, cliente=cliente, precio=precio_total)
        referencia_producto = request.POST["productos"]
        producto = Producto.objects.get(referencia=referencia_producto)
        cantidad = int(request.POST["cantidad"])
        linea_pedido = LineaPedido.objects.create(
            producto=producto, cantidad=cantidad, pedido=pedido)
        precio_total = round(producto.precio * cantidad, 2)
        pedido.precio = precio_total
        pedido.save()
    return redirect("/pedidos")


def ediccionPedido(request, referencia):
    pedido = Pedido.objects.get(referencia=referencia)
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    linea_pedido = LineaPedido.objects.get(pedido=pedido)
    print(linea_pedido)
    return render(request, "pedidos/ediccion_pedido.html", {'pedido': pedido, 'clientes': clientes, 'productos': productos, 'linea_pedido': linea_pedido})


def editarPedido(request):
    id_pedido = request.POST["referencia"]
    fecha = request.POST["fecha"]
    cliente_cif = request.POST["cliente"]
    producto_referencia = request.POST["productos"]
    cantidad = request.POST["cantidad"]

    pedido = Pedido.objects.get(referencia=id_pedido)
    pedido.fecha = fecha
    pedido.cliente = Cliente.objects.get(cif=cliente_cif)

    producto = Producto.objects.get(referencia=producto_referencia)

    # de momento asumimos que habra una sola linea de pedido y solo una
    lp = pedido.lineapedido_set.all()[0]

    lp.cantidad = cantidad
    lp.producto = producto

    lp.save()
    pedido.save()
    return redirect("/pedidos")
