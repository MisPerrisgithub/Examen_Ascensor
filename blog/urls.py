from django.conf.urls import include, url
from .views import index, registrar_cliente,registrar_orden,registro,listadoCliente,listadoOrden
from django.contrib.auth import login
from .views import  user_login, logOut, Login


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^Orden', registrar_orden, name='registrarOrden'),
    url(r'^Tecnico', registro, name='registro'),
    url(r'^Cliente', registrar_cliente, name='registrarCliente'),
    url(r'^Login', Login, name='Login'),
    url(r'^salir/$', logOut, name='logOut'),
    url(r'^user_login/$',user_login,name='user_login'),
    url(r'^listadoOrden', listadoOrden, name='listado_orden'),
    url(r'^listadoCliente', listadoCliente, name='listadoCliente'),
    ]
