from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Marca, Producto

from .forms import MarcaForm, ProductoForm

# Create your views here.

def crudMarca(request):
    marca = Marca.objects.all()
    context = {"marca":marca}
    return render(request,'test.html', context)

def crudProducto(request):
    producto = Producto.objects.all()
    context = {"producto":producto}
    return render(request,'test.html', context)