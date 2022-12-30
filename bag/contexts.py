from django.conf import settings
from django.shortcuts import get_object_or_404
from stock.models import Item

def bag_contents(request):

    bag_items = []
    total = 0
    item_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        item = get_object_or_404(Item, pk=item_id)
        total += item_data * item.price
        item_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'item': item,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_count': item_count,
        'grand_total': grand_total,
    }

    return context
    