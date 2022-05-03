from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Banner,Category,Product,ProductAttribute
from django.db.models import Max,Min,Count
from django.template.loader import render_to_string
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

#Filter data
def filter_data(request):
	colors=request.GET.getlist('color[]')
	categories=request.GET.getlist('category[]')
	sizes=request.GET.getlist('size[]')
	minPrice=request.GET['minPrice']
	maxPrice=request.GET['maxPrice']
	allProducts=Product.objects.all().order_by('-id').distinct()
	allProducts=allProducts.filter(productattribute__price__gte=minPrice)
	allProducts=allProducts.filter(productattribute__price__lte=maxPrice)
	if len(colors)>0:
		allProducts=allProducts.filter(productattribute__color__id__in=colors).distinct()
	if len(categories)>0:
		allProducts=allProducts.filter(category__id__in=categories).distinct()
	if len(sizes)>0:
		allProducts=allProducts.filter(productattribute__size__id__in=sizes).distinct()
	t=render_to_string('ajax/product-list.html',{'data':allProducts})
	return JsonResponse({'data':t})

# Product list
def product_list(request):
	total_data=Product.objects.count()
	data=Product.objects.all().order_by('-id')[:3]
	min_price=ProductAttribute.objects.aggregate(Min('price'))
	max_price=ProductAttribute.objects.aggregate(Max('price'))
	return render(request,'product_list.html',
		{
			'data':data,
			'total_data':total_data,
			'min_price':min_price,
			'max_price':max_price,
		}
		)

#Load more
def load_more_data(request):
	offset=int(request.GET['offset'])
	limit=int(request.GET['limit'])
	print(offset, limit)
	data = Product.objects.all().order_by('-id')[offset:offset+limit]
	t=render_to_string('ajax/product-list.html', {'data': data})
	return JsonResponse({'data': t})