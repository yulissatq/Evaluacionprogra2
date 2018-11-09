from django.shortcuts import render, redirect

# Create your views here.

from .forms import FormularioEstuadiante
from app.modelo.models import Estuadiante
from django.http import HttpResponse

def principal(request):
    usuario = request.user
    listaEst= Estuadiante.objects.all().order_by('nombres')
    context = {
            'lista': listaEst,
        }
    return render(request, 'estuadiantes/principal_estudiante.html', context)
    

def crear(request):
    formulario = FormularioEstuadiante(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            estudiante = Estuadiante()
            estudiante.cedula = datos.get('cedula')
            estudiante.nombres = datos.get('nombres')
            estudiante.apellidos = datos.get('apellidos')
            estudiante.edad = datos.get('edad')
            estudiante.direccion = datos.get('direccion')
            estudiante.save()
            return redirect(principal)

    context={
        'f': formulario,
        'mensaje': 'Bienvenidos', 
    }
    return render(request, 'estuadiantes/crear_estudiante.html', context)


