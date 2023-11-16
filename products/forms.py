from django import forms
from .models import ProductReview

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['product', 'rating', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['class'] = 'form-control'