from django.contrib import admin
from .models import Product, Category, Wishlist, ProductReview

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



class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'date_published')
    list_filter = ('product', 'rating', 'date_published')
    search_fields = ('product__name', 'user__username', 'text')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)