from django import forms
from .models import CustomBoardOrder


class CustomOrderForm(forms.ModelForm):
    class Meta:
        model = CustomBoardOrder
        fields = ['board_type', 'board_class', 'board_length', 'board_width', 'board_thickness', 'image_upload', 'board_color', 'additional_notes']
        widgets = {'board_color': forms.TextInput(attrs={'type': 'color'}), 'image_upload': forms.FileInput()}
        labels = {
            'board_length': 'Board Length (cm)',
            'board_width': 'Board Width (cm)',
            'board_thickness': 'Board Thickness (cm)',
            'image_upload': 'Upload Image to be printed on your board'
        }
