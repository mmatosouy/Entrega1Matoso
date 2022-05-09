from django.http import HttpResponse
from django.shortcuts import render
from appvet.forms import MascotaFormulario, pedidosFormulario, UsuarioFormulario
from appvet.models import Mascota, Pedidos, Usuario


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

def mascotas(request):

    
    if request.method == 'POST':    

        miFormulario = MascotaFormulario(request.POST)   

        print(miFormulario)

        if miFormulario.is_valid():    

            informacion = miFormulario.cleaned_data

            mascota = Mascota(nombre=informacion['nombre'], raza=informacion['raza'], 
            nacimiento=informacion['nacimiento'], descripcion=informacion['descripcion']) 

            mascota.save() 

            return render(request, "appvet/inicio.html")  

    else:

        miFormulario = MascotaFormulario()    


    return render(request, "appvet/mascota.html", {"miFormulario":miFormulario})


def pedidos(request):

    
    if request.method == 'POST':    

        miFormulario = pedidosFormulario(request.POST)   

        print(miFormulario)

        if miFormulario.is_valid():    

            informacion = miFormulario.cleaned_data

            pedidos = Pedidos(nombre=informacion['nombre'], email=informacion['email'], telefono=informacion['telefono'], pedido=informacion['pedido']) 

            pedidos.save() 

            return render(request, "appvet/inicio.html")  

    else:

        miFormulario = pedidosFormulario()    


    return render(request, "appvet/pedidos.html", {"miFormulario":miFormulario})

def inicio(request):

    return render(request,"appvet/inicio.html")

def busquedaPedido(request):

    return render(request, "appvet/busquedaPedido.html")

def buscar(request):

    if request.GET['pedido']:

        pedido = request.GET['pedido']
        Pedidos = Pedidos.objects.filter(Pedidos_icontains=pedido)

        return render(request, "appvet/resultadosBusqueda.html", {"Pedidos":Pedidos, "pedido":pedido})

    else:

        respuesta = "No enviaste el dato correcto"
    
    return HttpResponse(respuesta)
