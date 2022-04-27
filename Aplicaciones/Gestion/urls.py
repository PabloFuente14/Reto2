from django.urls import path
from . import views 


urlpatterns = [
    path('', views.inicio),
    path('categorias', views.categorias), 
    path('registrarCategoria/', views.registrarCategoria),
    path('ediccionCategoria/<id>',views.ediccionCategoria),
    path('editarCategoria/',views.editarCategoria),
    path('borrarCategoria/<id>',views.borrarCategoria),
]
