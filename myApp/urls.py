
from django.contrib import admin
from django.urls import path

# Views
from .views import bienvenido, despedido, saludo, saludar_con_nombre,kodemia_mentor

# su ruta http:127.0.0.1.8000


urlpatterns = [
    #cutomer URLS
    path ("despedido/", despedido),
    path ("", bienvenido),
    path("saludo/", saludo),
    path("saludo/<str:nombre>",saludar_con_nombre),
    path("kodemia/<str:type>", kodemia_mentor),
    
]
