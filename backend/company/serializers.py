from django.db.models import Sum
from rest_framework import serializers

from .models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.SerializerMethodField()
    salary_sum = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = (
            'pk',
            'name',
            'employee_count',
            'salary_sum',
        )

    def get_employee_count(self, obj):
        return obj.employee_set.count()

    def get_salary_sum(self, obj):
        aggregate = obj.employee_set.aggregate(salary_sum=Sum('salary'))
        return aggregate.get('salary_sum')


class EmployeeSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'pk',
            'first_name',
            'last_name',
            'middle_name',
            'position',
            'salary',
            'age',
            'department',
        )

    def get_position(self, obj):
        return obj.get_position_display()
