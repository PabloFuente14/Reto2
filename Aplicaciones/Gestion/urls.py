from django.urls import path
from . import views 


urlpatterns = [
    path('', views.inicio),
    
    #CATEGORIAS 
    path('categorias', views.categorias), 
    path('registrarCategoria/', views.registrarCategoria),
    path('ediccionCategoria/<id>',views.ediccionCategoria),
    path('editarCategoria/',views.editarCategoria),
    path('borrarCategoria/<id>',views.borrarCategoria),
    
    # COMPONENTES
    path('componentes', views.componentes), 
    path('registrarComponente/', views.registrarComponente),
    path('ediccionComponente/<id>',views.ediccionComponente),
    path('editarComponente/',views.editarComponente),
    path('borrarComponente/<id>',views.borrarComponente),
    
]
