from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from stock.models import Item
# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified item to the shopping bag """

    item = get_object_or_404(Item, pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[item_id] = quantity
    messages.success(request, f'Added {item.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
    
    
def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        item = get_object_or_404(Item, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {item.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
