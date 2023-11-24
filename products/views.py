from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#wishlist views
from django.contrib.auth.decorators import login_required
from .models import Wishlist, ProductReview

#product review form
from .forms import ProductReviewForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


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

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 12)  
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

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
    
    current_product = Product.objects.get(id=product_id)
    similar_products = Product.objects.filter(category=current_product.category).exclude(id=product_id)[:3]

    context = {
        'product': current_product,
        'similar_products': similar_products,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


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


class SubmitReviewView(LoginRequiredMixin, View):
    template_name = 'submit_review.html'
    login_url = '/accounts/login/'  

    def get(self, request):
        form = ProductReviewForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProductReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  
            review.save()
            return redirect('view_reviews')  

        return render(request, self.template_name, {'form': form})

