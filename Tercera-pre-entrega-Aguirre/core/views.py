from django.shortcuts import render
from . import forms

# Create your views here.

def home(request):
    return render(request, "core/index.html")

def agregarclientes(request):
    if request.method == "POST":
        form = forms.ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/index.html")
    else:
        form = forms.ClientesForm()
    return render(request, "core/agregarclientes.html", {"form" : form} )
