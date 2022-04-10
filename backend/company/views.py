from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
import django_filters.rest_framework

from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from .filters import EmployeeFilterSet


class EmployeeViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = EmployeeFilterSet
    permission_classes = [IsAuthenticated]


class DepartmentViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [AllowAny]
    pagination_class = None
