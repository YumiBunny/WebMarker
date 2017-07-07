# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Producto
from .models import Categoria
from .models import Compra

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Compra)


# Register your models here.
