from django.urls import path
from appvet import views


urlpatterns = [

    path("usuario/", views.usuario, name='Usuario'),
    path("mascota/", views.mascota, name="Mascota"),
    path("pedido/", views.pedido, name='Pedidos'),
    path("", views.inicio, name='Inicio'),
    path("busquedaApellido/", views.busquedaApellido, name="BusquedaApellido"),
    path("buscar/", views.buscar),
]
