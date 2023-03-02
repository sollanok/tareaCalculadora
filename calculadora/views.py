from django.shortcuts import render
from django.http import HttpResponse
from .models import tareaCalculadora
# excentar la necesidad de un token con POST
from django.views.decorators.csrf import csrf_exempt
# importar json
from json import loads, dumps

# Creación de clase Fracción
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def toJSON(self):
        return dumps(self, default = lambda o:o.__dict__, sort_keys = False, indent = 4)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return render(request, 'proceso.html',{'name':nombre})

# Creación de calculadora de fracciones
@csrf_exempt
def suma(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']

    # Proceso de suma
    # Denominadores iguales
    if denominador1 == denominador2:
        resultadoNum = numerador1 + numerador2
        resultado = Fraccion(resultadoNum, denominador1)
    # Denominadores diferentes
    else:
        resultadoDen = denominador1 * denominador2
        resultadoNum = (resultadoDen * numerador1 / denominador1) + (resultadoDen * numerador2 / denominador2)
        resultado = Fraccion(int(resultadoNum), resultadoDen)

    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
                        content_type = "text/json-comment-filtered")

@csrf_exempt
def resta(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']

    # Proceso de resta
    # Denominadores iguales
    if denominador1 == denominador2:
        resultadoNum = numerador1 - numerador2
        resultado = Fraccion(resultadoNum, denominador1)
    # Denominadores diferentes
    else:
        resultadoDen = denominador1 * denominador2
        resultadoNum = (resultadoDen * numerador1 / denominador1) - (resultadoDen * numerador2 / denominador2)
        resultado = Fraccion(int(resultadoNum), resultadoDen)

    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
                        content_type = "text/json-comment-filtered")

@csrf_exempt
def multiplicacion(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']

    # Proceso de multiplicación
    resultadoNum = numerador1 * numerador2
    resultadoDen = denominador1 * denominador2
    resultado = Fraccion(resultadoNum, resultadoDen)

    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
                        content_type = "text/json-comment-filtered")

@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    numerador1 = body['numerador1']
    denominador1 = body['denominador1']
    numerador2 = body['numerador2']
    denominador2 = body['denominador2']

    # Proceso de división
    resultadoNum = numerador1 * denominador2
    resultadoDen = denominador1 * numerador1
    resultado = Fraccion(resultadoNum, resultadoDen)

    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
                        content_type = "text/json-comment-filtered")
