from django.http import HttpResponse
from django.shortcuts import render
from appvet.forms import UsuarioFormulario
from appvet.models import Usuario


def usuario(request):

    
    if request.method == 'POST':    

        miFormulario = UsuarioFormulario(request.POST)   

        print(miFormulario)

        if miFormulario.is_valid():    

            informacion = miFormulario.cleaned_data

            usuario = Usuario(nombre=informacion['nombre'], apellido=informacion['apellido'], 
            email=informacion['email'], telefono=informacion['telefono'], direccion=informacion['direccion'])  #creando un curso (modelo) usando la info recibida

            usuario.save()

            return render(request, "appvet/inicio.html")  

    else:

        miFormulario = UsuarioFormulario()    


    return render(request, "appvet/usuario.html", {"miFormulario":miFormulario})

def mascota(request):

    return render(request, "appvet/mascota.html")

def pedido(request):

    return render(request, "appvet/pedido.html")

def inicio(request):

    return render(request,"appvet/inicio.html")

def busquedaApellido(request):

    return render(request, "appvet/busquedaUsuario.html")

def buscar(request):

    
    if request.GET['apellido']:

        apellido = request.GET['apellido']  
        usuario = Usuario.objects.filter(apellido__iexact=apellido)

        return render(request, "appvet/resultadosBusqueda.html", {"usuario":usuario, "apellido":apellido})

    else:

        respuesta="No enviaste datos."
    
    return HttpResponse(respuesta)
