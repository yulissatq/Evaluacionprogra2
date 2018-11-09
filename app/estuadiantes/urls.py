from django.urls import path

from . import views

urlpatterns =[
    path('', views.principal, name='estudiantes'),
    path('crear', views.crear,name="crear"),
   
]