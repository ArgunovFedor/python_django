import random

from django.shortcuts import render
from advertisements_app.models import Advertisement


def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    advertisement = advertisements[random.randint(0, len(advertisements) - 1)]
    return render(request, 'advertisements/advertisement_list.html', {
        'advertisements': advertisements,
        'random_advertisement': advertisement
    })
