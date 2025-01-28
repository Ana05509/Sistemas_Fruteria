from django.contrib import admin

from .models import Productos, Clientes, Ventas,Categoria

# Register your models here.

admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Ventas)
admin.site.register(Categoria)

