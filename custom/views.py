from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomBoardOrder
from .forms import CustomOrderForm


# Create your views here.

@login_required
def custom_orders(request):
    orders = CustomBoardOrder.objects.filter(user=request.user)
    return render(request, 'custom/custom_orders.html', {'custom_orders': orders})



def create_custom_order(request):
    if request.method == 'POST':
        form = CustomOrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user  
            form.save()
            return redirect('custom_orders')
    else:
        form = CustomOrderForm()

    return render(request, 'custom/create_custom.html', {'form': form})
