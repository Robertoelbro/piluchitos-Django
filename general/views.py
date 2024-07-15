from django.shortcuts import render

# Create your views here.

def i1(request):
    context={}
    return render(request, 'i1.html', context)

def nosotros(request):
    context={}
    return render(request, 'nosotros.html', context)

def sesion(request):
    context={}
    return render(request, 'sesion.html', context)

def productos(request):
    context={}
    return render(request, 'productos.html', context)

def inicio_adm(request):
    context={}
    return render(request, 'inicio_adm.html', context)

def creacion(request):
    context={}
    return render(request, 'creacion.html', context)