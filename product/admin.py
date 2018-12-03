from django.contrib import admin

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']
    list_filter = ['productname']
    search_fields = ['productname', 'producter']


admin.site.register(Product, ProductAdmin)
