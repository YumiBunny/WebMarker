# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Producto
from .models import Categoria

admin.site.register(Producto)
admin.site.register(Categoria)


# Register your models here.
