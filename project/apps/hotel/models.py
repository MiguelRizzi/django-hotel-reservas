from django.db import models

# Create your models here.
class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo de habitacion"
        verbose_name_plural = "Tipos de habitaciones"

    def __str__(self):
        return self.nombre
    
class Habitacion(models.Model):
    tipo = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(unique=True)
    precio_x_dia = models.DecimalField(max_digits=10, decimal_places=2,)
    disponible = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to="img/", null=True, blank=True)

    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"

    def __str__(self):
        return f"Habitacion N° {self.numero}"