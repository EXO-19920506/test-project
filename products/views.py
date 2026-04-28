from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, render

from .models import Product


def index(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'shop/index.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_active=True)
    return render(request, 'shop/product_detail.html', {'product': product})


@staff_member_required
def admin_product_list(request):
    q = request.GET.get('q', '')
    products = Product.objects.all()
    if q:
        products = products.filter(name__icontains=q)
    return render(request, 'admin/product_list.html', {'products': products, 'q': q})
