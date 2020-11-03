"""
Pantalla de login
Vistas de Users
"""
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def logon(request):
    return render(request, 'login.html')