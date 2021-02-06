import django_filters
from .models import *


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = order
        fields = '__all__'
        exclude=['customer','date_created']