from django.shortcuts import render
from app_shops.models import Shop


# Create your views here.

def page_with_cached_fragments(request):
    shops = Shop.objects.all()
    return render(request, 'page_with_cached_fragments.html', context={
        'shops': shops
    })
