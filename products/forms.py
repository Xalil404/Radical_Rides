from django import forms
from .widgets import CustomClearableFileInput
from .models import ProductReview

from .models import Product, Category

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['product', 'rating', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'