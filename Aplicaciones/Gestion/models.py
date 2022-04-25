import datetime
from django.db import models

# Create your models here.

class Componente (models.Model):
    referencia= models.CharField(primary_key=True, max_length=45)
    nombre=models.CharField(max_length=200)
    marca=models.CharField(max_length=200)


class Categoria (models.Model):
    nombre=models.CharField(max_length=200)

class Producto (models.Model):
    referencia=models.CharField(primary_key=True, max_length=45)
    precio=models.DecimalField(max_digits=6, decimal_places=2)
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField()
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE) 
    componentes=models.ManyToManyField(Componente)

class Cliente (models.Model):
    cif=models.CharField(primary_key=True, max_length=45)
    nombre=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    ciudad=models.CharField(max_length=200)
    telefono=models.IntegerField()
    correo=models.EmailField()

class Pedido (models.Model):
    referencia=models.CharField(primary_key=True, max_length=45)
    fecha=models.DateField(default=datetime.date.today)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE) 
    precio=models.DecimalField(max_digits=10, decimal_places=2)

class LineaPedido (models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE) 
    cantidad=models.IntegerField()
    pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE) 