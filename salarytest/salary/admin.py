from django.contrib import admin
from .models import Department, Employee, SalaryHistory

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'departmentName', 'parentId', 'createAt')
    search_fields = ('departmentName',)
    ordering = ('id',)
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName', 'email', 'phoneNumber', 'hireDate', 'salary', 'departmentId', 'createAt')
    search_fields = ('firstName', 'lastName', 'email')
    ordering = ('id',)
    
@admin.register(SalaryHistory)
class SalaryHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'employeeId', 'oldSalary', 'salary', 'changeDate', 'changedBy')
    search_fields = ('employeeId__firstName', 'employeeId__lastName', 'changedBy')
    ordering = ('id',)
    