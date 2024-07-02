"""
URLs general
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('i1', views.i1, name='i1'),
]