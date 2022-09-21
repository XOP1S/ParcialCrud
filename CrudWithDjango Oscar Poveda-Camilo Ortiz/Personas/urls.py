from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('registrarPacientes/', views.registrarPacientes),
    path('editarPaciente/<codigo>', views.editarPaciente),
    path('edicionPacientes/', views.edicionPacientes),
    path('eliminarPaciente/<codigo>', views.eliminarPaciente)
]