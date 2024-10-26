from django.contrib import admin
from .models import Ingrediente, Coctel, Receta, Trabajador

# Register your models here.

admin.site.register(Ingrediente)
admin.site.register(Coctel)
admin.site.register(Receta)
admin.site.register(Trabajador)