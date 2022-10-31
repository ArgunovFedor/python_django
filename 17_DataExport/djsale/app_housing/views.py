from django.views import generic
from django.core import serializers
from django.http import HttpResponse

from app_housing.models import Housing


# Create your views here.
def list_of_housing_for_sale(request):
    data = serializers.serialize('json', Housing.objects.all())
    return HttpResponse(data)


class HousingDetailView(generic.DetailView):
    model = Housing
    template_name = 'housing/housing_detail.html'


class HousingItemsView(generic.ListView):
    model = Housing
    context_object_name = 'housing_list'
    queryset = Housing.objects.all()[:5]
    template_name = 'housing/housing_list.html'
