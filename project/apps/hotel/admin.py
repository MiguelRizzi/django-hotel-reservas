from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_title = "El Jardin Secreto"
admin.site.site_header = "El Jardin Secreto Administración"
admin.site.index_title = "Panel de control"

class HabitacionInline(admin.TabularInline):
    model = models.Habitacion
    extra = 0

class ReservaInline(admin.TabularInline):
    model = models.Reserva
    extra = 0


@admin.register(models.TipoHabitacion)
class TipoHabitacionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion",)
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)
    inlines = [HabitacionInline]


@admin.register(models.Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Relación", {"fields": ["tipo"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'numero', 'precio_x_dia', 'disponible' , 'imagen'
                ]
            },
        ),
    ]
    list_display = (
        "tipo",
        "numero",
        "precio_x_dia",
        "disponible",
        "imagen",
    )
    search_fields = ("tipo__nombre","numero",)
    list_filter = ("tipo__nombre", "disponible",)
    ordering = ("tipo","-numero",)
    list_display_links=("tipo","numero",)
    inlines = [ReservaInline]


@admin.register(models.Reserva)
class ReservaAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Relación", {"fields": ["cliente", "habitacion"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'Fecha_entrada', 'Fecha_salida'
                    ]
            },
        ),
    ]
    list_display = (
        "cliente",
        "habitacion",
        "fecha_entrada",
        "fecha_salida",
        "precio_total",
    )
    search_fields = ("cliente__username", "habitacion__tipo__nombre",)
    list_filter = ("fecha_entrada", "fecha_salida")
    list_display_links=("cliente","habitacion",)
    ordering = ("-fecha_entrada",)


