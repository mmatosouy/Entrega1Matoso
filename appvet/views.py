from django.http import HttpResponse
from django.shortcuts import render
from appvet.forms import MascotaFormulario, PedidoFormulario, UsuarioFormulario, RegistroFormulario
from appvet.models import Mascotas, Pedidos, Usuarios
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate


def usuario(request):

    
    if request.method == 'POST':    

        miFormulario = UsuarioFormulario(request.POST)   

        print(miFormulario)

        if miFormulario.is_valid():    

            informacion = miFormulario.cleaned_data

            usuario = Usuarios(nombre=informacion['nombre'], apellido=informacion['apellido'], 
            email=informacion['email'], telefono=informacion['telefono'], direccion=informacion['direccion'])  #creando un curso (modelo) usando la info recibida

            usuario.save()

            return render(request, "appvet/inicio.html")  

    else:

        miFormulario = UsuarioFormulario()    


    return render(request, "appvet/usuario.html", {"miFormulario":miFormulario})

def mascota(request):

    
    if request.method == 'POST':    

        miFormulario = MascotaFormulario(request.POST)   

        print(miFormulario)

        if miFormulario.is_valid():    

            informacion = miFormulario.cleaned_data

            mascota = Mascotas(nombre=informacion['nombre'], raza=informacion['raza'], 
            nacimiento=informacion['nacimiento'], descripcion=informacion['descripcion']) 

            mascota.save() 

            return render(request, "appvet/mascotaFormulario.html")  

    else:

        miFormulario = MascotaFormulario()    


    return render(request, "appvet/mascota.html", {"miFormulario":miFormulario})


def pedido(request):

    
    if request.method == 'POST':    

        miFormulario = PedidoFormulario(request.POST)   

        print(miFormulario)

        if miFormulario.is_valid():    

            informacion = miFormulario.cleaned_data

            pedido = Pedidos(nombre=informacion['nombre'], email=informacion['email'], 
            telefono=informacion['telefono'], pedido=informacion['pedido']) 

            pedido.save() 

            return render(request, "appvet/inicio.html")  

    else:

        miFormulario = PedidoFormulario()    


    return render(request, "appvet/pedido.html", {"miFormulario":miFormulario})

def inicio(request):

    return render(request,"appvet/inicio.html")

def busquedaApellido(request):

    return render(request, "appvet/busquedaApellido.html")

def buscar(request):

    #respuesta = f"Estoy buscando usuarios con el apellido: {request.GET['apellido']}"
   
    if request.GET["apellido"]:

        apellido = request.GET['apellido']  
        usuario = Usuarios.objects.filter(apellido__iexact=apellido)

        return render(request, "appvet/resultadosBusqueda.html", {"usuario":usuario, "apellido":apellido})

    else:

        respuesta="No enviaste datos."
    
    return HttpResponse(respuesta)
