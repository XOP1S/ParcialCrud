import re
from django.shortcuts import render, redirect
from .models import Paciente

# Create your views here.
def home(request):
    pacientesListados = Paciente.objects.all()
    return render(request, "gestionPaciente.html", {"pacientes": pacientesListados} )

def registrarPacientes(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    edad = request.POST['txtEdad']
    peso = request.POST['txtPeso']
    bpm = request.POST['txtBpm']
    oxigeno = request.POST['txtOxigeno']
    stress = request.POST['txtStress']

    
    paciente = Paciente.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, edad=edad, peso=peso, bpm=bpm, oxigeno=oxigeno, stress=stress)
    return redirect('/')

def eliminarPaciente(request, codigo):
    paciente = Paciente.objects.get(codigo=codigo)
    paciente.delete()
    return redirect('/')
    
def edicionPacientes(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    edad = request.POST['txtEdad']
    peso = request.POST['txtPeso']
    bpm = request.POST['txtBpm']
    oxigeno = request.POST['txtOxigeno']
    stress = request.POST['txtStress']
   
    
    paciente = Paciente.objects.get(codigo=codigo)
    paciente.nombre = nombre
    paciente.apellido = apellido
    paciente.edad = edad
    paciente.peso = peso
    paciente.bpm = bpm
    paciente.oxigeno = oxigeno
    paciente.stress = stress
    paciente.save()
    return redirect('/')

def editarPaciente(request, codigo):
    paciente = Paciente.objects.get(codigo=codigo)
    return render(request, "editarPaciente.html", {"paciente": paciente})