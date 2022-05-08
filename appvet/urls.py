from django.urls import path
from appvet import views


urlpatterns = [

    path("usuario/", views.usuario, name='Usuario'),
    path("mascota/", views.mascotas, name="Mascota"),
    path("pedido/", views.pedido, name='Pedidos'),
    path("", views.inicio, name='Inicio'),
    #path("cursoFormulario/", views.cursoFormulario, name="CursoFormulario"),
    path("busquedaApellido/", views.busquedaApellido, name="BusquedaApellido"),
    path("buscar/", views.buscar),
]
