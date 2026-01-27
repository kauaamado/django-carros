from django.shortcuts import render
from cars.models import Car

# ~~~~{ Views da página /cars }~~~~ #

def cars_view(request):
    cars = Car.objects.all()

    return render(
        request,
        'cars.html',
        {'cars': cars}
    )