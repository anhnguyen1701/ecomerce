from typing import Sized
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_text', 'image_tag')
admin.site.register(Banner, BannerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'status', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Product, ProductAdmin)

#productAttribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','image_tag','product','price', 'color', 'size')
admin.site.register(ProductAttribute, ProductAttributeAdmin)

# Order
class CartOrderAdmin(admin.ModelAdmin):
	list_editable=('paid_status','order_status')
	list_display=('user','total_amt','paid_status','order_dt','order_status')
admin.site.register(CartOrder,CartOrderAdmin)
class CartOrderItemsAdmin(admin.ModelAdmin):
	list_display=('invoice_no','item','image_tag','qty','price','total')
admin.site.register(CartOrderItems,CartOrderItemsAdmin)

class ProductReviewAdmin(admin.ModelAdmin):
	list_display=('user','product','review_text','get_review_rating')
admin.site.register(ProductReview,ProductReviewAdmin)


admin.site.register(Wishlist)

class UserAddressBookAdmin(admin.ModelAdmin):
	list_display=('user','address','status')
admin.site.register(UserAddressBook,UserAddressBookAdmin)