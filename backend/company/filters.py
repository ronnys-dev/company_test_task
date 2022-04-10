from django_filters import filters, filterset

from .models import Employee


class EmployeeFilterSet(filterset.FilterSet):
    last_name = filters.CharFilter(lookup_expr='icontains', field_name='last_name')

    class Meta:
        model = Employee
        fields = [
            'last_name',
            'department',
        ]
