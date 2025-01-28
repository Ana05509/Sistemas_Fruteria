from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)  
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Clientes(models.Model):
    cedula = models.IntegerField(unique=True)  
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Ventas(models.Model):
    ci_cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    ci_producto = models.ForeignKey('Productos', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta de {self.ci_producto.nombre} a {self.ci_cliente.nombre}"
