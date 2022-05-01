from django.contrib import admin
from .models import Usuario
from .models import Mascota
from .models import Pedido

admin.site.register(Usuario)
admin.site.register(Mascota)
admin.site.register(Pedido)

# Register your models here.
