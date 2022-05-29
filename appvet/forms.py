from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    telefono = forms.CharField()
    direccion = forms.CharField()
    

class MascotaFormulario(forms.Form):

    nombre = forms.CharField()
    raza = forms.CharField()
    nacimiento= forms.DateField()
    descripcion = forms.CharField()
   
class PedidoFormulario(forms.Form):

    nombre = forms.CharField()
    email = forms.EmailField()
    telefono = forms.CharField()
    pedido = forms.CharField()

class RegistroFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 