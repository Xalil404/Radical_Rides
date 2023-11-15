from django.contrib import admin
from .models import Product, Category, Wishlist

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'display_products')

    def display_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])

    display_products.short_description = 'Products'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist, WishlistAdmin)