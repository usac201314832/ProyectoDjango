"""
Pantalla de login
Vistas de Users
"""
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect

def logon(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            userSession = authenticate(request, username = username, password = password)
            if userSession:
                login(request, userSession)
                return redirect("homepage")
            else:
                return render(request, 'login.html', {'error' : "Su usuario o contraseña es incorrecto"})
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect("logon")