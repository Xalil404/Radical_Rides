from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.
#wishlist views
from django.contrib.auth.decorators import login_required
from .models import Wishlist, ProductReview


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def view_wishlists(request):
    user_wishlists = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlists.html', {'user_wishlists': user_wishlists})


def view_wishlist(request, wishlist_id):
    wishlist = Wishlist.objects.get(id=wishlist_id, user=request.user)
    products = wishlist.products.all()
    return render(request, 'view_wishlist.html', {'wishlist': wishlist, 'products': products})


def wishlist_add(request, wishlist_id):
    wishlist = Wishlist.objects.get(id=wishlist_id, user=request.user)
    all_products = Product.objects.all()

    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('products')
        selected_products = Product.objects.filter(id__in=selected_product_ids)
        wishlist.products.add(*selected_products)
        return redirect('view_wishlist', wishlist_id=wishlist_id)

    return render(request, 'wishlist_add.html', {'wishlist': wishlist, 'all_products': all_products})


def create_wishlist(request):
    if request.method == 'POST':
        # Process the form submission to create a new wishlist
        wishlist_name = request.POST.get('wishlist_name')
        if wishlist_name:
            new_wishlist = Wishlist.objects.create(user=request.user, name=wishlist_name)
            return redirect('select_products', wishlist_id=new_wishlist.id)

    return render(request, 'create_wishlist.html')


def select_products(request, wishlist_id):
    wishlist = Wishlist.objects.get(id=wishlist_id, user=request.user)
    all_products = Product.objects.all()

    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('products')
        selected_products = Product.objects.filter(id__in=selected_product_ids)
        wishlist.products.add(*selected_products)
        return redirect('view_wishlist', wishlist_id=wishlist_id)

    return render(request, 'select_products.html', {'wishlist': wishlist, 'all_products': all_products})


def delete_wishlist(request, wishlist_id):
    wishlist = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)

    if request.method == 'POST':
        wishlist.delete()
    return redirect('view_wishlists')


def remove_from_wishlist(request, wishlist_id, product_id):
    wishlist = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        wishlist.products.remove(product)
    
    return redirect('view_wishlist', wishlist_id=wishlist_id)


def view_reviews(request):
    reviews = ProductReview.objects.select_related('product').all().order_by('-date_published')
    return render(request, 'view_reviews.html', {'reviews': reviews, 'star_range': range(5)})  