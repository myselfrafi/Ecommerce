from django.contrib import admin

from products.models import Product



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=[p.name for p in Product._meta.fields]