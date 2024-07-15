"""
URLs general
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('i1', views.i1, name='i1'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('productos',views.productos,name='productos'),
    path('sesion',views.sesion,name='sesion'),
    path('creacion',views.creacion,name='creacion'),
    path('inicio_adm',views.inicio_adm,name='inicio_adm'),
]