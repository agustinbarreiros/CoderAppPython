from django.http import HttpResponse
from django.template import loader

def saludo(request):
    return HttpResponse("Hola mundo xDDDD")


def segunda_vista(request):
    return HttpResponse("<h1> AWEBOOOO </h1>")

def miNombre(self, nombre):
    data = f"Mi nombre es : <h2>{nombre}</h2>"
    return HttpResponse(data)

def probandotemplate(self):
    diccionario = {"nombre": "agustin", "apellido": "barreiros"}
   # miHtml = open('D:/Coding/python/DJANGO/Proyecto1/Proyecto1/plantillas/template1.html')
    ##la forma mas facil en realidad es 
    plantilla = loader.get_template("template1.html")
    # Hay que rutear la direccion del template en DIR en settings
    document = plantilla.render(diccionario) #de esa manera, evitas todas las lineas extra de codigo
   # plantilla = Template(miHtml.read())
   # miHtml.close()
   # miContext = Context(diccionario)
   #document = plantilla.render(miContext)
    return HttpResponse(document)