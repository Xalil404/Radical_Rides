from django.contrib import admin
from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('custom_orders/', views.custom_orders, name='custom_orders'),
    path('create_custom/', views.create_custom_order, name='create_custom'),
    path('view_order/<int:order_id>/', views.view_order, name='view_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
