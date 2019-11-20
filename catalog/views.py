from django.shortcuts import render
from .models import Producer, ElectronicType, ElectronicInstance, Electronic


def index(request):
    num_electronics = Electronic.objects.all().count()
    num_instances = ElectronicInstance.objects.all().count()
    num_instances_available = ElectronicInstance.objects.filter(status__exact='a').count()
    num_producers = Producer.objects.count()
    num_electronics_type = ElectronicType.objects.count()

    return render(
        request,
        'index.html',
        context={'num_electronics': num_electronics,
                 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_producers': num_producers,
                 'num_electronics_type': num_electronics_type},
    )
