from django.urls import path
from .views import EmployeeManagement,DepartmentManagement


rest_api_url = [
    path('department/',DepartmentManagement.department_management, name='departmentmanagement'),
    path('modelserializer/',EmployeeManagement.employee_model, name='modelserializer'),
    path('serializermethod/',EmployeeManagement.employee_serializermethod, name='serializermethod'),
]

urlpatterns = rest_api_url
