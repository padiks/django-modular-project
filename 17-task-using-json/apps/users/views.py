from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings  # import settings for redirects

def login_view(request):
    """
    Display login page. On POST, authenticate user.
    Redirect to LOGIN_REDIRECT_URL on success.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            # Redirect to movements home page as set in settings.py
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'users/login.html')


def logout_view(request):
    """
    Log out user and redirect to LOGOUT_REDIRECT_URL.
    """
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
