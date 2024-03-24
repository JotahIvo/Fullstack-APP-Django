from django.contrib import admin
from cars.models import Car, Brand


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'plate', 'value')
    search_fields = ('model', )
    list_per_page = 20

admin.site.register(Car, CarAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_per_page = 20

admin.site.register(Brand, BrandAdmin)