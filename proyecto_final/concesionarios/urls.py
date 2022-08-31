from sqlite3 import Cursor
from django.urls import path
from .views import *

urlpatterns=[
    path("concesionario/",concesionario),
    path("clienteFormulario/",clienteFormulario,name="clienteFormulario"),
    path("autoFormulario/",autoFormulario,name="autoFormulario"),
    path("sucursalFormulario/",sucursalFormulario,name="sucursalFormulario"),
    path("busquedaSucursal/",busquedaSucursal,name="busquedaSucursal"),
    path("busquedaCliente/",busquedaCliente,name="busquedaCliente"),
    path("busquedaAuto/",busquedaAuto,name="busquedaAuto"),
    path("buscar_sucursal/",buscar_sucursal,name="buscar_sucursal"),
    path("buscar_auto/",buscar_auto,name="buscar_auto"),
    path("buscar_cliente/",buscar_cliente,name="buscar_cliente"),
]