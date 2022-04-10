from rest_framework.routers import DefaultRouter

from company.views import EmployeeViewSet, DepartmentViewset

router = DefaultRouter()

router.register('employee', EmployeeViewSet, basename='employee')
router.register('department', DepartmentViewset, basename='department')

urlpatterns = router.urls
