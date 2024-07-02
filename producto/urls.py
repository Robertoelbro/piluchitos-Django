"""
URLs producto
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('crudMarca',views.crudMarca,name='crudMarca'),
    path('crudProducto',views.crudProducto,name='crudProducto'),
]