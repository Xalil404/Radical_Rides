from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('liked-products/', views.liked_products, name='liked_products'),
    path('like-product/<int:product_id>/', views.like_product, name='like_product'),
    path('unlike-product/<int:product_id>/', views.unlike_product, name='unlike_product'),
]
