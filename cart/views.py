from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from products.models import Product

from .services import add_to_cart, iter_items, merge_session_to_user, remove_item, total_price, update_qty


@require_POST
def add_item(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    qty = max(1, int(request.POST.get('qty', 1)))

    if qty > product.stock:
        messages.error(request, f'{product.name} 库存不足，当前库存为 {product.stock}。')
        return redirect('shop:product_detail', pk=product.id)

    add_to_cart(request, product, qty)
    messages.success(request, f'已加入购物车：{product.name}')
    return redirect('cart:cart_detail')


def cart_detail(request):
    if request.user.is_authenticated:
        merge_session_to_user(request)
    items = list(iter_items(request))
    return render(request, 'cart/cart.html', {'items': items, 'total': total_price(request)})


@require_POST
def update_item(request, product_id):
    qty = int(request.POST.get('qty', 1))
    update_qty(request, product_id, qty)
    return redirect('cart:cart_detail')


@require_POST
def delete_item(request, product_id):
    remove_item(request, product_id)
    return redirect('cart:cart_detail')
