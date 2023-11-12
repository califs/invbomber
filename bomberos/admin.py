from django.contrib import admin

# Register your models here.
from .models import Articulos
from .models import BodegaCentral
from .models import Distribucion
from .models import InvVeh
from .models import Personal
from .models import TipoUsuario
from .models import Vehiculo
from .models import BomberosArticulos

admin.site.register(Articulos)
admin.site.register(BodegaCentral)
admin.site.register(BomberosArticulos)
admin.site.register(Distribucion)
admin.site.register(InvVeh)
admin.site.register(Personal)
admin.site.register(TipoUsuario)
admin.site.register(Vehiculo)
