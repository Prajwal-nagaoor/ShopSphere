from django.contrib import admin
from .models import productsmodel,category,cartmodel
# Register your models here.

class productadminmodel(admin.ModelAdmin):
    list_display=['product_category','product_name','product_desc','product_price','product_image']
admin.site.register(productsmodel,productadminmodel)

class cartadminmodel(admin.ModelAdmin):
    list_display=['product_category','product_name','product_desc','product_price','product_image','quantity','price','host']
admin.site.register(cartmodel,cartadminmodel)

class categorymodel(admin.ModelAdmin):
    list_display=['category_name']
admin.site.register(category,categorymodel)