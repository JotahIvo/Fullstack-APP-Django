from django.shortcuts import render
from cars.models import Car

#django ORM and querysets https://docs.djangoproject.com/pt-br/4.2/topics/db/
def cars_view(request):
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')
        
        if not cars:
            cars = Car.objects.filter(brand__name__icontains=search).order_by('model')
    else:
        cars = Car.objects.all().order_by('model')

    print(cars)

    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )
