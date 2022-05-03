from django.shortcuts import render
from .models import *
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
    cats = Product.objects.distinct().values('category__title', 'category__id')
    colors = ProductAttribute.objects.distinct().values('color__title', 'color__id', 'color__color_code')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size__id')

    return render(request, 'product_list.html', {
        'data': data,
        'cats': cats,
        'colors': colors,
        'sizes': sizes
    })

# Product list according to Category
def category_product_list(request, cat_id):
	category=Category.objects.get(id=cat_id)
	data=Product.objects.filter(category=category).order_by('-id')
	cats=Product.objects.distinct().values('category__title','category__id')
	colors=ProductAttribute.objects.distinct().values('color__title','color__id','color__color_code')
	sizes=ProductAttribute.objects.distinct().values('size__title','size__id')
	return render(request,'category_product_list.html',{
			'data':data,
			'cats':cats,
			'colors':colors,
			'sizes':sizes,
			})

# Product detail
def product_detail(request, slug, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'data': product})