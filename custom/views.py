from django.shortcuts import render

# Create your views here.

def custom(request):
    """ A view to return the custom boards page """

    return render(request, 'custom/custom.html')