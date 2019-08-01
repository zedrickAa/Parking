from django.db import models
class Cliente(models.Model):
    DPI = models.CharField(max_length=16)
    nombre = models.CharField(max_length=60)
    NIT = models.CharField(max_length=20)
    Direccion = models.TextField()

    def __str__(self):
        return self.nombre + "/" + self.DPI  

class Vehiculo(models.Model):
    placa = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    propietario = models.ForeignKey(Cliente, on_delete = models.PROTECT)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.placa + " Entrada: " + str(self.hora_inicio) + "Salida: " + str(self.hora_fin)