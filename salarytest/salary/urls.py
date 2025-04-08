from django.urls import path, include
from . import views

urlpatterns = [
    path("salary/", views.employeeList, name='employeeList'),
    path('updateSalary/<int:id>', views.updateSalary, name='updateSalary'),
    path('get_employees/', views.get_employees, name='get_employees'),
    #########################################################################
    path('salary2/', views.salary_update_view, name='salary_update'),
    path('employees/', views.employees, name='employees'),
    path('deleteemployee/', views.deleteEmployees, name='deleteEmployees'),
    path('get_employees/', views.get_employees, name='get_employees'),
    path('get_salary/', views.get_salary, name='get_salary'),
    # path('update_salary/', views.update_salary, name='update_salary'),
    path('update_salary/', views.update_salary_proc, name='update_salary'),
    path('salary_complete/<int:emp_id>/', views.salary_complete, name='salary_complete'),
]
