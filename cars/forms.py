from django import forms
from cars.models import Brand, Car


""" class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    image = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            image = self.cleaned_data['image'],
        )
        car.save() #insert in database

        return car """
    

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


    def clean_value(self): #validation function 'clean_...()'
        value = self.cleaned_data.get('value')
        if value < 15000:
            self.add_error('value', 'O valor mínimo do carro deve ser R$15.000,00')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1970:
            self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1970')
        return factory_year
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image == None:
            self.add_error('image', 'Adicione uma imagem do seu veículo')
        return image