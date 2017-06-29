# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Producto


def producto_list(request):
    productovar = Producto.objects.all()
    return render(request, 'producto/pag.html', {'producto': productovar})

# Create your views here.
