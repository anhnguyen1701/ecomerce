from django.http import HttpResponse
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
    related_products=Product.objects.filter(category=product.category).exclude(id=id)[:4]
    return render(request, 'product_detail.html', {'data': product,'related':related_products})

# Search
def search(request):
    q = request.GET['q']
    data = Product.objects.filter(title__icontains=q).order_by('-id')
    return render(request, 'search.html', {'data': data})

#Filter Products
def filter_product(request):
    colors = request.GET.getlist('color[]')
    categories = request.GET.getlist('category[]')
    sizes = request.GET.getlist('size[]')
    filterProducts = ProductAttribute.objects.filter(
        color__id__in = colors,
        product__category__id__in = categories
		# size__id__in=sizes,
    )
    return HttpResponse(filterProducts.query)
    # return JsonResponse({'data':list(filterProducts)})