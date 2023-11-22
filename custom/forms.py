from django import forms
from .models import CustomBoardOrder 


class CustomOrderForm(forms.ModelForm):
    class Meta:
        model = CustomBoardOrder
        fields = ['board_type', 'board_class', 'board_length', 'board_width', 'board_thickness', 'image_upload', 'board_color', 'additional_notes']
        widgets = {'board_color': forms.TextInput(attrs={'type': 'color'}), 'image_upload': forms.FileInput()}
        labels = {'image_upload': 'Upload Image'}
        
