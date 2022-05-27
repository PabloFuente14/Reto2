import datetime
from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Componente (models.Model):
    referencia= models.CharField(primary_key=True, max_length=45)
    nombre=models.CharField(max_length=200)
    marca=models.CharField(max_length=200)

    def __str__(self):
        return f"referencia: {self.referencia}, nombre: {self.nombre}, marca: {self.marca}"


class Categoria (models.Model):
    nombre=models.CharField(max_length=200)

    def __str__(self):
        return f"nombre: {self.nombre}"

class Producto (models.Model):
    referencia=models.CharField(primary_key=True, max_length=45)
    precio=models.DecimalField(max_digits=6, decimal_places=2)
    nombre=models.CharField(max_length=200)
    descripcion=models.TextField()
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE) 
    componentes=models.ManyToManyField(Componente)
    # Añadido entrega3, type imagen-->guarda la imagen
    imagen=models.ImageField(upload_to='productos',null=True)
    
    def __str__(self):
        return f" referencia: {self.referencia}, precio: {self.precio}, nombre: {self.nombre}, descripcion: {self.descripcion}, categoria: {self.categoria}, componentes: {self.componentes}"
        

class Cliente (models.Model):
    cif=models.CharField(primary_key=True, max_length=45)
    nombre=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    cp=models.IntegerField()
    ciudad=models.CharField(max_length=200)
    provincia=models.CharField(max_length=200)
    telefono=models.IntegerField()
    correo=models.EmailField()

    def __str__(self):
        return self.cif
        #return self.cif, self.nombre, self.direccion, self.ciudad, self.telefono, self.correo


class Pedido (models.Model):
    referencia=models.CharField(primary_key=True, max_length=45)
    fecha=models.DateField(default=datetime.date.today)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE) 
    precio=models.DecimalField(max_digits=10, decimal_places=2)

class LineaPedido (models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE) 
    cantidad=models.IntegerField()
    pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE) 