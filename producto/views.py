# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

    def producto_list(request):
        return render(request, 'blog/producto_list.html', {})

# Create your views here.
