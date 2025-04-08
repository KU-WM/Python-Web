from django import forms
from .models import Department, Employee, SalaryHistory

class DepartmentFrom(forms.ModelForm):
    class Meta:
        model=Department
        fields = ['id', 'departmentName', 'parentId']
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields = ['id', 'firstName', 'lastName', 'email', 'phoneNumber', 'salary', 'departmentId']
        
class SalaryHistoryForm(forms.ModelForm):
    class Meta:
        model=SalaryHistory
        fields = ['employeeId','salary', 'changedBy']