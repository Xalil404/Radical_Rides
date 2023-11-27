from django.contrib import admin
from .models import CustomBoardOrder

# Register your models here.


class CustomBoardOrderAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email', 'board_type', 'board_class', 'board_length', 'board_width', 'board_thickness', 'image_upload', 'board_color', 'additional_notes')

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email

    get_username.admin_order_field = 'user__username'
    get_username.short_description = 'Username'

    get_email.admin_order_field = 'user__email'
    get_email.short_description = 'Email'


admin.site.register(CustomBoardOrder, CustomBoardOrderAdmin)
