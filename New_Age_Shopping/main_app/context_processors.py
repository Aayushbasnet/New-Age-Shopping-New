from .models import Level1ProductCategory,OrderItem


def navbar_category(request):
    level1_objects =   Level1ProductCategory.objects.filter().distinct()
    if request.user.is_authenticated:
        add_to_cart_bubbles = OrderItem.objects.filter(user = request.user, complete = False).count()
    else:
        add_to_cart_bubbles = '0'

    context =   {
        "level1_objects"   :   level1_objects,
        'add_to_cart_bubbles' : add_to_cart_bubbles,
    }   

    return context