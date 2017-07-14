# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Producto


def producto_list(request):
    productovar = Producto.objects.all()
    return render(request, 'producto/pag.html', {'productos': productovar})

def contacto(request):
    return render(request, 'producto/contacto.html', {})

def productos(request):
    productovar = Producto.objects.all()
    return render(request, 'producto/productos.html', {'productos': productovar})

def datos(request,pk):
    productovar = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto/datos.html', {'producto': productovar})

