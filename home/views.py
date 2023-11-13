from django.shortcuts import render, redirect
from .models import ContactMessage
from .forms import ContactForm 

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """ A view to handle the contact form and display the contact page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            success_message = "Thank you for your message! We will get in touch with you soon."
            return render(request, 'home/contact.html', {'form': ContactForm(), 'success_message': success_message})
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})