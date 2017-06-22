# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre_de_producto = models.CharField(max_length=200)
    categoria = models.ForeignKey('Categorias')
    precio = models.IntegerField()
    stock = model.IntegerField()
    vencimiento = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.nombre_de_producto

class Compra(models.Model):
    cantidad_de_producto = models.IntegerField()
    precio_total = models.IntegerField()

class Categorias(models.Model):
    categoria = models.CharField(max_length=40)

    def __str__(self):
        return self.categoria


# Create your models here.
