from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path("agregarproducto/", views.agregarproducto, name="agregarproducto"),
    path("agregarmarca/", views.agregarmarca, name="agregarmarca"),
    path("crearmarca/", views.crearmarca),
    path("crearproducto/", views.crearproducto),
    path("busqueda/", views.buscar_productos, name="busqueda")
]