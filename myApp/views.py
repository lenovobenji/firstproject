from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#cliente--> pide -->Requeste

def bienvenido(request):
    #respoder
    return HttpResponse("bienvenido")
    
def despedido(request):
    return HttpResponse("despedido")
    
def saludo (request):
    return HttpResponse("Saludando a Koders")


def saludar_con_nombre(request,nombre):
    print(nombre)
    return HttpResponse(f"Hola {nombre}")

def kodemia_mentor (request,type):
    
    if type == "mentor":
        return HttpResponse("Hello mentor here are your casses")
    
    elif type == "koder":
        return HttpResponse("Hello koder welcome to kodemia")
    
    else:   
         return HttpResponse("You are not welcome here")
