from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name ="index"),
    path("agregarclientes/", views.agregarclientes, name="agregar")
]