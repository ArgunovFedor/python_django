import random

from django.shortcuts import render
from advertisements_app.models import Advertisement
from django.views.generic import ListView, DetailView


def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    advertisement = advertisements[random.randint(0, len(advertisements) - 1)]
    return render(request, 'advertisements/advertisement_list.html', {
        'advertisements': advertisements,
        'random_advertisement': advertisement
    })


class AdvertisementListView(ListView):
    template_name = 'advertisements/advertisement_list.html'
    model = Advertisement
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]


class AdvertisementDetailView(DetailView):
    template_name = 'advertisements/advertisement_detail.html'
    model = Advertisement
    context_object_name = 'advertisement_detail'
