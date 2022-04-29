from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio),

    # CATEGORIAS
    path('categorias', views.categorias),
    path('registrarCategoria/', views.registrarCategoria),
    path('ediccionCategoria/<id>', views.ediccionCategoria),
    path('editarCategoria/', views.editarCategoria),
    path('borrarCategoria/<id>', views.borrarCategoria),

    # COMPONENTES
    path('componentes', views.componentes),
    path('registrarComponente/', views.registrarComponente),
    path('ediccionComponente/<referencia>', views.ediccionComponente),
    path('editarComponente/', views.editarComponente),
    path('borrarComponente/<referencia>', views.borrarComponente),

    # PRODUCTOS
    path('productos', views.productos),
    path('registrarProducto/', views.registrarProducto),
    path('ediccionProducto/<referencia>',views.ediccionProducto),
    # path('editarProducto/',views.editarProducto),
    # path('borrarProducto/<referencia>',views.borrarProducto),

    # Clientes
    path('clientes', views.clientes),
    path('registrarCliente/', views.registrarCliente),
    path('ediccionCliente/<cif>', views.ediccionCliente),
    path('editarCliente/',views.editarCliente),
    path('borrarCliente/<cif>',views.borrarCliente),



]
