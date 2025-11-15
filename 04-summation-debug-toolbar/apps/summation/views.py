# apps/summation/views.py
#from django.shortcuts import render

# **Guide 2 Step 3: Register the app in `settings.py`**
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, this is the Summation app!")

# **Guide 3 Step 7**
from django.shortcuts import render

def index(request):
    return render(request, 'summation/index.html')

