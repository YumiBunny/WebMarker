from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.producto_list, name="views.home"),
    url(r'^contacto$', views.contacto, name="producto.views.contacto"),
    url(r'^productos$', views.productos, name="views.productos"),
    url(r'^datos/(?P<pk>[0-9]+)/$', views.datos, name="views.datos"),
]
