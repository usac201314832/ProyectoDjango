"""
    Archivo general de vistas del proyecto
    Login/homepage
"""
from django.http import HttpResponse

def homepage(request):
    return HttpResponse ("Bienvenido a la pagina principal")
