from .services import iter_items


def cart_summary(request):
    count = sum(item['quantity'] for item in iter_items(request))
    return {'cart_item_count': count}
