from django.shortcuts import render

# Create your views here.

#Homepage
def home(request):
    return render(request, 'index.html')