
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_grid(request):
    products = Product.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.all().order_by('name')
    return render(request, 'shop/product-grid.html', {'products': products, 'categories': categories})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'shop/product-detail.html', {'product': product})
