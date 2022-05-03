from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('category-list', views.category_list, name='category-list'),
    path('product-list', views.product_list, name='product-list')
]