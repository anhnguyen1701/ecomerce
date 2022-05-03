from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('search',views.search,name='search'),
    path('category-list', views.category_list, name='category-list'),
    path('product-list', views.product_list, name='product-list'),
    path('category-product-list/<int:cat_id>',views.category_product_list,name='category-product-list'),
    path('product/<str:slug>/<int:id>',views.product_detail,name='product_detail'),
]