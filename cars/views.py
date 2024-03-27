from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm

#django ORM and querysets https://docs.djangoproject.com/pt-br/4.2/topics/db/
def cars_view(request):
    search = request.GET.get('search')

    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')
        
        if not cars:
            cars = Car.objects.filter(brand__name__icontains=search).order_by('model')
    else:
        cars = Car.objects.all().order_by('model')

    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES) #image
        
        if new_car_form.is_valid():
            new_car_form.save() #method function at forms.py
            return redirect('cars_list')
        else:
            return render(
                request,
                'new_car.html',
                {'new_car_form': new_car_form}
            )
    
    if request.method == 'GET':
        new_car_form = CarModelForm()

        return render(
            request, 
            'new_car.html',
            {'new_car_form': new_car_form}
        )