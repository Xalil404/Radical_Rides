from django.urls import path
from . import views

from .views import all_products, product_detail, view_wishlists, view_wishlist, wishlist_add, create_wishlist, select_products, delete_wishlist, remove_from_wishlist, view_reviews, SubmitReviewView

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('wishlists/', views.view_wishlists, name='view_wishlists'),
    path('view_wishlist/<int:wishlist_id>/', views.view_wishlist, name='view_wishlist'),
    path('wishlist/<int:wishlist_id>/add/', wishlist_add, name='wishlist_add'),
    path('create_wishlist/', create_wishlist, name='create_wishlist'),
    path('select_products/<int:wishlist_id>/', select_products, name='select_products'),
    path('delete_wishlist/<int:wishlist_id>/', delete_wishlist, name='delete_wishlist'),
    path('remove_from_wishlist/<int:wishlist_id>/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('view_reviews/', view_reviews, name='view_reviews'),
    path('submit_review/', SubmitReviewView.as_view(), name='submit_review'),
]