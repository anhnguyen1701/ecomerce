from typing import Sized
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'title','brand', 'color', 'size', 'status')
admin.site.register(Product, ProductAdmin)
