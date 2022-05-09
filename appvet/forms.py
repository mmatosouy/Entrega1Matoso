from django import forms

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
   
class pedidosFormulario(forms.Form):

    nombre = forms.CharField()
    email = forms.EmailField()
    telefono = forms.CharField()
    pedido = forms.CharField()