from email.mime import image
from unicodedata import category
from django.db import models
from django.utils.html import mark_safe

# Create your models here.
#todo : delete brand

#Banner
class Banner(models.Model):
    img=models.ImageField(upload_to="banner_imgs/")
    alt_text=models.CharField(max_length=300)

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text

#Category
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cat_imgs/')

    def __str__(self):
        return self.title


#Color
class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.title

#Size
class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

#Product
class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=400)
    detail = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)

    def __str__(self):
        return self.title

#Product Attribute
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color=models.ForeignKey(Color, on_delete=models.CASCADE)
    size=models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_imgs/')

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.product.title