from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


from django.http import JsonResponse


# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            del bag[item_id]
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def liked_products(request):
    liked_product_ids = request.session.get('liked_product_ids', [])
    liked_products = Product.objects.filter(id__in=liked_product_ids)

    liked_product_ids = [product.id for product in liked_products]

    context = {'liked_products': liked_products, 'liked_product_ids': liked_product_ids}
    return render(request, 'bag/liked_products.html', context)


def like_product(request, product_id):
    liked_product_ids = request.session.get('liked_product_ids', [])
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        if product_id not in liked_product_ids:
            liked_product_ids.append(product_id)
            request.session['liked_product_ids'] = liked_product_ids

    return JsonResponse({'success': True, 'message': 'Product liked successfully'})


def unlike_product(request, product_id):
    liked_product_ids = request.session.get('liked_product_ids', [])
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        if product_id in liked_product_ids:
            liked_product_ids.remove(product_id)
            request.session['liked_product_ids'] = liked_product_ids

    return redirect('liked_products')
