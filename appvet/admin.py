from django.contrib import admin
from .models import Usuarios
from .models import Mascotas
from .models import Pedidos

admin.site.register(Usuarios)
admin.site.register(Mascotas)
admin.site.register(Pedidos)


