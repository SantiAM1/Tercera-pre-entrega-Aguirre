from django import forms
from . import models

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"

class MarcaForm(forms.ModelForm):
    class Meta:
        model = models.Marca
        fields = "__all__"

class ProductoBuscar(forms.Form):
    nombre = forms.CharField()
