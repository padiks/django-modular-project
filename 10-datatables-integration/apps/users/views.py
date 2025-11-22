# apps/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')  # or 'uom:index'
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
