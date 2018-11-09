from django import forms

from app.modelo.models import Estuadiante

class FormularioEstuadiante(forms.ModelForm):
    class Meta:
        model = Estuadiante
        fields = ["cedula", "nombres", "apellidos","edad", "direccion"]