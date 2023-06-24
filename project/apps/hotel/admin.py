from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_title = "El Jardin Secreto"
admin.site.site_header = "El Jardin Secreto Admin"

@admin.register(models.TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)


@admin.register(models.Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = (
        "tipo",
        "numero",
        "precio_x_dia",
        "disponible",
        "imagen",
    )
    
    search_fields = ("tipo__nombre","numero",)
    list_filter = ("tipo__nombre",)
    ordering = (
        "tipo",
        "numero",
    )