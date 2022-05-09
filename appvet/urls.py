from django.urls import path
from appvet import views


urlpatterns = [

    path("usuario/", views.usuario, name='Usuario'),
    path("mascota/", views.mascotas, name="Mascota"),
    path("pedidos/", views.pedidos, name='Pedidos'),
    path("", views.inicio, name='Inicio'),
    #path("cursoFormulario/", views.cursoFormulario, name="CursoFormulario"),
    path("busquedaPedido/", views.busquedaPedido, name="busquedaPedido"),
    path("buscar/", views.buscar),
]
