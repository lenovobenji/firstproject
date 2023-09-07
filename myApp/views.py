from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


#cliente--> pide -->Requeste

def bienvenido(request):
    #respoder
    return HttpResponse("bienvenido")
    
def despedido(request):
    return HttpResponse("despedido")
    
def saludo (request):
    return HttpResponse("Saludando a Koders")


def saludar_con_nombre(request,):
    context = {"name": nombre, "apellido":"Aguilar"}
    template = loader.get_template("templates/base.html")
    return HttpResponse (template.render(context, request))

def kodemia_mentor (request,type):
    
    if type == "mentor":
        return HttpResponse("Hello mentor here are your casses")
    
    elif type == "koder":
        return HttpResponse("Hello koder welcome to kodemia")
    
    else:   
         return HttpResponse("You are not welcome here")
     

     
     
          
