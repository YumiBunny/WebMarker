# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria

class Producto(models.Model):
    nombredeproducto = models.CharField(max_length=200)
    categoria = models.ForeignKey('Categoria')
    precio = models.IntegerField()
    stock = models.IntegerField()
    vencimiento = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombredeproducto

class Compra(models.Model):
    cantidad_de_producto = models.IntegerField()
    precio_total = models.IntegerField()




# Create your models here.
