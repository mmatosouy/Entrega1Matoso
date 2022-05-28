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


def register(request):

    if request.method == 'POST':    
        form = RegistroFormulario(request.POST)   

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "appvet/inicio.html", {'mensaje':"Tu usuario se creo exitosamente"})
    
    else:

        form = RegistroFormulario()  
    
    
    return render(request, "appvet/registro.html", {'form':form})


def login_request(request):

    if request.method == 'POST': 

        form = AuthenticationForm(request, data = request.POST) 
        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')  
            contra=form.cleaned_data.get('password')    

            user=authenticate(username=usuario, password=contra)    
            if user: 

                login(request, user)   
                return render(request, "appvet/inicio.html", {'mensaje':f"Hola {user}"}) 

        else:  

            return render(request, "appvet/inicio.html", {'mensaje':"Error. Los datos son incorrectos"})

    else:
            
        form = AuthenticationForm() 

    return render(request, "appvet/login.html", {'form':form})    



# LO REFERENTE AL USUARIO

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


def editarUsuario(request):

    usuario = request.user 

    if request.method == "POST":    

        miFormulario = RegistroFormulario(request.POST) 

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data     

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "appvet/inicio.html")

    else:

        miFormulario= RegistroFormulario(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "appvet/editarUsuario.html",{'miFormulario':miFormulario, 'usuario':usuario.username})

def busquedaApellido(request):

    return render(request, "appvet/busquedaApellido.html")

def buscar(request):

    if request.GET["apellido"]:

        apellido = request.GET['apellido']  
        usuario = Usuarios.objects.filter(apellido__iexact=apellido)

        return render(request, "appvet/resultadosBusqueda.html", {"usuario":usuario, "apellido":apellido})

    else:

        respuesta="No enviaste datos."
    
    return HttpResponse(respuesta)

class UsuarioList(LoginRequiredMixin, ListView):

    model = usuario
    template_name = "appvet/listaUsuario.html"

class UsuarioDetalle(DetailView):

    model = usuario
    template_name = "appvet/usuarioDetalle.html"

class UsuarioCreacion(CreateView):

    model = usuario
    success_url = "/appvet/usuario/lista"
    fields = ['nombre', 'appellido', 'email']

class UsuarioUpdate(UpdateView):

    model = usuario
    success_url = "/appvet/usuario/lista"
    fields = ['nombre', 'appellido', 'email']

class UsuarioDelete(DeleteView):

    model = usuario
    success_url = "/appvet/usuario/lista"

#LO REFERENTE A LAS MACOTAS

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

#LO REFERENTE A LOS PEDIDOS

@login_required
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

    dict1={"miFormulario":miFormulario} 

    return render(request, "appvet/pedido.html", dict1)

def inicio(request):

    return render(request,"appvet/inicio.html")

def aboutus(request):

    return render(request,"appvet/aboutus.html")




