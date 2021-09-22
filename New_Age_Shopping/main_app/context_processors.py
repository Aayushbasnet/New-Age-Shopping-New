from .models import Level1ProductCategory


def navbar_category(request):
    level1_objects =   Level1ProductCategory.objects.filter().distinct()

    context =   {
        "level1_objects"   :   level1_objects,
    }   

    return context