
from django.shortcuts import render
from service.models import Service
from workers.models import Salon, Social


def salon_listes(request):
    salons = Salon.objects.all()
    ctx = {
        'salons' : salons,
    }
    return render(request, 'salons/list.html', ctx)

def salon_detail(request, num_salon):
    salon = Salon.objects.get(id=num_salon)
    socials = Social.objects.filter(salon_id=num_salon)
    services = Service.objects.filter(salon_id=num_salon)
    ctx = {
        'salon' : salon,
        'socials' : socials,
        'services' : services,
    }
    return render(request, 'salons/detail.html', ctx)

def salon_filter(request, name):
    salon = Salon.objects.get(name=name)
    ctx = {
        'salon' : salon,
    }
    return render(request, 'salons/filter.html', ctx)    
