from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Marca, Producto
from .forms import MarcaForm, ProductoForm

# Create your views here.

def crudMarca(request):
    marca = Marca.objects.all()
    context = {"marca":marca}
    return render(request,'marcas_list.html', context)

def inMarca(request):
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            form=MarcaForm()
            msg='Marca ingresada correctamente'
            context={"form":form,'msg':msg}
            return render(request,'inserta_marca.html',context)
    else:
        form = MarcaForm()
        context={"form":form}
        return render(request,'inserta_marca.html',context)
    
def borraMarca(request,pk):
    try:
        marca=Marca.objects.get(id_marca=pk)
        marca.delete()
        marcas=Marca.objects.all()
        context={'marcas':marcas}
        return redirect('crudMarca')

    except:
        msg='Marca no existente'    
        marcas=Marca.objects.all()
        context={'marcas':marcas,'msg':msg}
        return render(request,'marcas_list.html',context) 

def modMarca(request,pk):
    try:
        marca=Marca.objects.get(id_marca=pk)      
        if marca:
            if request.method == "POST":
                form = MarcaForm(request.POST,instance=marca)
                form.save()
                marcas=Marca.objects.all()
                contexto={'marcas':marcas}    
                return redirect('crudMarca')
            else:
                form = MarcaForm(instance=marca) 
                contexto={'form':form,'marca':marca}
                return render(request,'modifica_marca.html',contexto)    
    except:
        contexto={'msg','Error - La marca no existe'}
        return render(request,'marcas_list.html',contexto)
    

def crudProducto(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'productos_list.html', context)

def ingreso_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductoForm()
            msg = 'Se ha ingresado el producto correctamente'
            context = {"form":form}
            return render(request, 'ingreso_producto.html', context)
    else:
        form = ProductoForm()
        context = {"form": form}
        return render(request, 'ingreso_producto.html', context)


def modifica_producto(request, codprod):
    producto = get_object_or_404(Producto, codprod=codprod)

    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('crudProducto')
    else:
        form = ProductoForm(instance=producto)

    context = {
        "form": form,
        "producto": producto
    }
    return render(request, 'modifica_producto.html', context)

def borra_producto(request,pk):
    context={}
    try:
        producto=Producto.objects.get(codprod=pk)
        producto.delete()
        msg='Producto Eliminado Exitosamente'
        productos=Producto.objects.all()
        context={'productos':productos,'msg':msg}
        return render(request,'productos_list.html',context)
    except:
        msg='Código de producto no utilizado'    
        productos=Producto.objects.all()
        context={'productos':productos,'msg':msg}
        return render(request,'productos_list.html',context)        
