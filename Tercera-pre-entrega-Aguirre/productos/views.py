from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.

def buscar_productos(request):
    if request.method == "GET":
        form = forms.ProductoBuscar()
        return render(request, "productos/busqueda.html", {"form" : form} )
    else:
        form = forms.ProductoBuscar(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            busqueda_filtrada = []
            for producto in models.Producto.objects.filter(nombre__contains=data["nombre"]):
                busqueda_filtrada.append(producto)
            context = {"busqueda" : busqueda_filtrada}
            return render(request, "productos/busqueda_list.html", context)

def agregarproducto(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:index")
    else:
        form = forms.ProductoForm()
    return render(request, "productos/agregarproducto.html", {"form" : form} )

def agregarmarca(request):
    if request.method == "POST":
        form = forms.MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:index")
    else:
        form = forms.MarcaForm()
    return render(request, "productos/agregarmarca.html", {"form" : form} )

def crearmarca(request):
    m1 = models.Marca(nombre="Intel")
    m2 = models.Marca(nombre="AMD")
    m3 = models.Marca(nombre="Asus")
    m1.save()
    m2.save()
    m3.save()
    return redirect("core:index")

def crearproducto(request):
    p1 = models.Producto(nombre="Ryzen 5", precio=100, stock=1, marca_id=2)
    p1.save()
    return redirect("core:index")