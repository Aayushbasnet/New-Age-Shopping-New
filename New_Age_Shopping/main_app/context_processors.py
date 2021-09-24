from .models import Level1ProductCategory,OrderItem


def navbar_category(request):
    level1_objects =   Level1ProductCategory.objects.filter().distinct()
    add_to_cart_bubbles = OrderItem.objects.all().count()

    context =   {
        "level1_objects"   :   level1_objects,
        'add_to_cart_bubbles' : add_to_cart_bubbles,
    }   

    return context