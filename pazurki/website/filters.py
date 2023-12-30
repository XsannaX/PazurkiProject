import django_filters
from django_filters import CharFilter
from .models import *


#filtrowanie zwierzat
class AnimalFilter(django_filters.FilterSet):
    name=CharFilter(field_name="name",lookup_expr='icontains',label='Name')
    breed = CharFilter(field_name="breed", lookup_expr='icontains', label='Breed')
    class Meta:
        model = Animal
        fields = ['name','breed','sex','age','size','vaccinations','sterilization','friendly_kids','friendly_others']