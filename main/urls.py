from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('search',views.search,name='search'),
    path('category-list', views.category_list, name='category-list'),
    path('product-list', views.product_list, name='product-list'),
    path('category-product-list/<int:cat_id>',views.category_product_list,name='category-product-list'),
    path('product/<str:slug>/<int:id>',views.product_detail,name='product_detail'),
    path('filter-data',views.filter_data,name='filter_data'),
    path('load-more-data', views.load_more_data, name='load_more_data'),
    path('cart',views.cart_list,name='cart'),
    path('delete-from-cart',views.delete_cart_item,name='delete-from-cart'),
    path('update-cart',views.update_cart_item,name='update-cart'),
]