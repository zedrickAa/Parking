from django.contrib import admin
from .models import Cliente,Vehiculo
from django.utils.safestring import mark_safe


admin.site.register(Vehiculo)
admin.site.register(Cliente)
