from django.db import models


# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=20, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    preferred_contact_method = models.CharField(
        max_length=20,
        choices=[
            ('email', 'Email'),
            ('phone', 'Phone Call'),
        ],
        null=False,
        blank=False,
        default='Email'
    )
    message = models.TextField(max_length=2000, blank=False, null=False)

    def __str__(self):
        return self.name
