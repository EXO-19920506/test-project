from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render

from cart.models import CartItem
from cart.services import iter_items, total_price

from .models import Order, OrderItem


@login_required
def checkout(request):
    items = list(iter_items(request))
    if not items:
        messages.warning(request, '购物车为空，无法下单。')
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        with transaction.atomic():
            order = Order.objects.create(user=request.user, total_amount=Decimal('0.00'))
            total = Decimal('0.00')
            for item in items:
                product = item['product']
                qty = item['quantity']
                if product.stock < qty:
                    messages.error(request, f'{product.name} 库存不足。')
                    order.delete()
                    return redirect('cart:cart_detail')
                product.stock -= qty
                product.save(update_fields=['stock'])
                OrderItem.objects.create(order=order, product=product, price=product.price, quantity=qty)
                total += product.price * qty

            order.total_amount = total
            order.save(update_fields=['total_amount'])
            CartItem.objects.filter(user=request.user).delete()

        return render(request, 'orders/order_success.html', {'order': order})

    return render(request, 'orders/checkout.html', {'items': items, 'total': total_price(request)})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')
    return render(request, 'orders/order_list.html', {'orders': orders})
