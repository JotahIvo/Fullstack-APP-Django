from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView


#django ORM and querysets https://docs.djangoproject.com/pt-br/4.2/topics/db/
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)
        return cars


""" class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()

        return render(
            request, 
            'new_car.html',
            {'new_car_form': new_car_form}
        )
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES) #image
        
        if new_car_form.is_valid():
            new_car_form.save() #method function at forms.py
            return redirect('cars_list')
    
        return render(
            request,
            'new_car.html',
            {'new_car_form': new_car_form}
        ) """
    

class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'