import email
from django.http import HttpResponse
from django.shortcuts import render
from appvet.forms import CursoFormulario, UsuarioFormulario
from appvet.models import Usuario


def usuario(request):

    
    if request.method == 'POST':    #al hacer click en enviar

        miFormulario = UsuarioFormulario(request.POST)    #aquí llega la info del formulario 

        print(miFormulario)

        if miFormulario.is_valid():     #comprobar si la info es valida

            informacion = miFormulario.cleaned_data

            usuario = Usuario(nombre=informacion['nombre'], apellido=informacion['apellodp'], 
            email=informacion['email'], telefono=informacion['telefono'], direccion=informacion['direccion'])  #creando un curso (modelo) usando la info recibida

            usuario.save()

            return render(request, "appvet/inicio.html")  #una vez guardado, mostramos la plantilla de inicio.    

    else:

        miFormulario = UsuarioFormulario()    #me muestra un formulario vacio


    return render(request, "appvet/usuario.html", {"miFormulario":miFormulario})

def mascota(request):

    return render(request, "appvet/mascota.html")

def pedido(request):

    return render(request, "appvet/pedido.html")

def inicio(request):

    return render(request,"appvet/inicio.html")

def buscar(request):

    #respuesta=f"Estoy buscando la camada {request.GET['camada']}"

    if request.GET['apellido']:

        apellido = request.GET['apellido']      #almacenar el número de camada que estamos buscando
        #cursos = Curso.objects.filter(camada__icontains=camada) #icontains significa que el numero que buscamos está contenido en la camada
        usuario = Usuario.objects.filter(apellido__iexact=apellido)

        return render(request, "appvet/resultadosBusqueda.html", {"usuario":usuario, "apellido":apellido})

    else:

        respuesta="No enaste vidatos."
    
    return HttpResponse(respuesta)
