import django_filters
from django_filters import DateFilter, CharFilter


from . models import *

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'final_cost', 'qty', 'cost','date_created']

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['final_cost', 'qty', 'cost','date_created']