from django.shortcuts import render
from .models import *
from django.db.models import Max,Min
# Create your views here.

#Homepage
def home(request):
    banners = Banner.objects.all().order_by('-id')
    data = Product.objects.filter(is_featured=True).order_by('-id')
    return render(request, 'index.html', {'data': data, 'banners': banners})

#Category
def category_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'category_list.html', {'data': data})

# Product list
def product_list(request):
    data = Product.objects.all().order_by('-id')
    min_price = ProductAttribute.objects.aggregate(Min('price'))
    max_price = ProductAttribute.objects.aggregate(Max('price'))

    return render(request, 'product_list.html', {
        'data': data,
        'min_price': min_price,
        'max_price': max_price
    })

# Product list according to Category
def category_product_list(request, cat_id):
	category=Category.objects.get(id=cat_id)
	data=Product.objects.filter(category=category).order_by('-id')
	return render(request,'category_product_list.html',{
			'data':data,
			})

# Product detail
def product_detail(request, slug, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'data': product})