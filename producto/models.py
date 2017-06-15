# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre_de_producto = models.CharField(max_length=200)
    descripcion = models.TextField()
    vencimiento = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.nombre_de_producto

# Create your models here.
