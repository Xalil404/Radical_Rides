from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IkpBDL1AEn5AiBuvyNyThoH1tBzBezsfLYsa6gQ5YK9BUsQy7wu5P6kbW97Qp9u7ms2ioS39jzY9LZhVRGUFJRe005TbFD7C0',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)