from django.urls import path
from appvet import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path("usuario/", views.usuario, name='Usuario'),
    path("mascota/", views.mascota, name="Mascota"),
    path("pedido/", views.pedido, name='Pedidos'),
    path("aboutus/", views.aboutus, name='aboutus'),
    path("contact/", views.contact, name='contact'),
    path("termsofuse/", views.termsofuse, name='termsofuse'),
    path("privacy/", views.privacy, name='privacy'),
    path("", views.inicio, name='Inicio'),
    path("busquedaApellido/", views.busquedaApellido, name="BusquedaApellido"),
    path("buscar/", views.buscar),

    path('pedido/lista', views.PedidoList.as_view(), name='ListPedidos'),
    path(r'^(?P<pk>\d+)$', views.PedidoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.PedidoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.PedidoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PedidoDelete.as_view(), name='Delete'),

    path('login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='appvet/logout.html'), name='Logout'),
    path('register', views.register, name = 'Register'),
    path("editarUsuario", views.editarUsuario, name="EditarUsuario"),

    path('leerUsuarios', views.leerUsuarios, name="leerUsuarios")

]

