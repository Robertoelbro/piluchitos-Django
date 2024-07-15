"""
URLs producto
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('crudMarca',views.crudMarca,name='crudMarca'),
    path('inserta_marca',views.inMarca,name='inserta_marca'),
    path('modifica_marca/<int:pk>',views.modMarca,name='modifica_marca'),
    path('borra_marca/<int:pk>',views.borraMarca,name='borra_marca'),
    path('crudProducto',views.crudProducto,name='crudProducto'),
    path('ingreso_producto',views.ingreso_producto, name='ingreso_producto'),
    path('modifica_producto<int:codprod>/',views.modifica_producto,name='modifica_producto'),
    path('borra_producto/<int:pk>',views.borra_producto,name='borra_producto'),
]