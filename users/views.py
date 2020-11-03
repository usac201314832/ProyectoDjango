"""
Vistas de Users
"""
from django.http import HttpResponse

def logon(request):
    return HttpResponse("Pagina de formulario de ingreso:")