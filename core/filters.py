import django_filters
from .models import *
from django_filters import DateFilter


class WorkEntryFilter(django_filters.FilterSet):
    """
    Filters WorkEntry by user , date range
    """
    start_date = DateFilter(field_name='date', lookup_expr='gte')
    end_date = DateFilter(field_name='date', lookup_expr='lte')
    class Meta:
        model = WorkEntry
        fields = '__all__'
        exclude = ['date', 'start_time', 'end_time']