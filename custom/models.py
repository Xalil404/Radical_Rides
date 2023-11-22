from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomBoardOrder(models.Model):
    BOARD_TYPES = [
        ('snow', 'Snowboard'),
        ('surf', 'Surfboard'),
        ('skate', 'Skateboard'),
    ]

    BOARD_CLASSES = [
        ('regular_skate', 'Regular Skate'),
        ('cruiser', 'Cruiser'),
        ('mini', 'Mini'),
        ('shortboard', 'Shortboard'),
        ('hybrid', 'Hybrid Board'),
        ('longboard', 'Longboard'),
        ('mens_snowboard', "Men's Snowboard"),
        ('womens_snowboard', "Women's Snowboard"),
        ('kids_snowboard', 'Kids Snowboard'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board_type = models.CharField(max_length=20, null=False, blank=False, choices=BOARD_TYPES)
    board_class = models.CharField(max_length=20, null=False, blank=False, choices=BOARD_CLASSES)
    board_length = models.IntegerField(null=False, blank=False)
    board_width = models.IntegerField(null=False, blank=False)
    board_thickness = models.IntegerField(null=False, blank=False)
    image_upload = models.ImageField(upload_to='custom_board_images/')
    board_color = models.CharField(null=False, blank=False, max_length=10)  
    additional_notes = models.TextField()

    def __str__(self):
        return f"{self.get_board_type_display()} - {self.get_board_class_display()}"
