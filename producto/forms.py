from django import forms
from .models import Marca, Producto

from django.forms import ModelForm

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"