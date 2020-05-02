from django.shortcuts import render
from .models import Services,Subservices,Example_photos
#from django.http import HttpResponse



def index(request):
    services = Services.objects.all()
    subservices = Subservices.objects.all()
    return render(request, 'photos/index.html', {'services': services,'subservices': subservices})


def subservice_example(request, pk):
    services = Services.objects.all()
    subservices = Subservices.objects.all()

    red = Subservices.objects.get(pk = pk)
    example = Example_photos.objects.filter(basic_subservice=red)
    return render(request, 'photos/index_s.html', {'services': services,'subservices': subservices,'red':red,'example': example})
