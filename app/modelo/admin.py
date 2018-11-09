from django.contrib import admin

# Register your models here.

from .models import Estuadiante
class AdminEstuadiante(admin.ModelAdmin):
    list_display = ["cedula", "nombres", "apellidos", "edad", "direccion"]
    list_editable = ["apellidos", "nombres", "edad", "direccion"]
    list_filter = ["apellidos"]
    search_fields = ["cedula", "nombres", "apellidos"]

    class Meta:
        model= Estuadiante

admin.site.register(Estuadiante, AdminEstuadiante)