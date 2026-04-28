from decimal import Decimal

from .models import CartItem

SESSION_CART_KEY = 'cart'


def _session_cart(request):
    return request.session.setdefault(SESSION_CART_KEY, {})


def add_to_cart(request, product, qty=1):
    if request.user.is_authenticated:
        item, _ = CartItem.objects.get_or_create(user=request.user, product=product)
        item.quantity += qty
        item.save()
        return

    cart = _session_cart(request)
    pid = str(product.id)
    cart[pid] = cart.get(pid, 0) + qty
    request.session.modified = True


def update_qty(request, product_id, qty):
    qty = max(0, int(qty))
    if request.user.is_authenticated:
        item = CartItem.objects.filter(user=request.user, product_id=product_id).first()
        if not item:
            return
        if qty == 0:
            item.delete()
        else:
            item.quantity = qty
            item.save()
        return

    cart = _session_cart(request)
    pid = str(product_id)
    if qty == 0:
        cart.pop(pid, None)
    else:
        cart[pid] = qty
    request.session.modified = True


def remove_item(request, product_id):
    update_qty(request, product_id, 0)


def iter_items(request):
    from products.models import Product

    if request.user.is_authenticated:
        items = CartItem.objects.filter(user=request.user).select_related('product')
        for item in items:
            subtotal = item.product.price * item.quantity
            yield {'product': item.product, 'quantity': item.quantity, 'subtotal': subtotal}
        return

    cart = _session_cart(request)
    products = Product.objects.filter(id__in=cart.keys())
    for p in products:
        qty = int(cart.get(str(p.id), 0))
        yield {'product': p, 'quantity': qty, 'subtotal': p.price * qty}


def total_price(request):
    total = Decimal('0.00')
    for item in iter_items(request):
        total += item['subtotal']
    return total


def merge_session_to_user(request):
    if not request.user.is_authenticated:
        return
    cart = request.session.get(SESSION_CART_KEY, {})
    from products.models import Product

    for pid, qty in cart.items():
        product = Product.objects.filter(id=pid).first()
        if product:
            item, _ = CartItem.objects.get_or_create(user=request.user, product=product)
            item.quantity += int(qty)
            item.save()
    request.session[SESSION_CART_KEY] = {}
    request.session.modified = True
