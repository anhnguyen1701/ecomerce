from django.shortcuts import render
from .models import *
# Create your views here.

#Homepage
def home(request):
    banners = Banner.objects.all().order_by('-id')
    data = Product.objects.all().order_by('-id')
    return render(request, 'index.html', {'data': data, 'banners': banners})

#Category
def category_list(request):
    data = Category.objects.all().order_by(-id)
    return render(request, 'category_list.html', {'data': data})