from .models import *
import uuid
# from django.http import request

def for_items_total(request):
    cart_items = OrderItem.objects.filter(user = request.user, complete = False)
    grand_total= 0
    for items in cart_items:
        grand_total = grand_total + float(items.get_total)

    items_total= 0
    for items in cart_items:
        items_total = items_total + 1

    return grand_total, items_total


def esewa_id():
    code = str(uuid.uuid4())
    return code