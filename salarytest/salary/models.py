from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True, db_column='dept_id')
    departmentName = models.CharField(max_length=100, db_column='dept_name')
    parentId = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, db_column='parent_dept_id', related_name='children')
    createAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    
    class Meta:
        db_table = 'departments'
        managed = False
    
    def __str__(self):
        return self.departmentName

class Employee(models.Model):
    id = models.AutoField(primary_key=True, db_column='emp_id')
    firstName = models.CharField(max_length=100, db_column='first_name')
    lastName = models.CharField(max_length=100, db_column='last_name')
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15, db_column='phone')
    hireDate = models.DateField(db_column='hire_date')
    salary = models.FloatField()
    departmentId = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_id')
    createAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    
    class Meta:
        db_table = 'employees'
        managed = False
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
class SalaryHistory(models.Model):
    id = models.AutoField(primary_key=True, db_column='hist_id')
    employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_id')
    oldSalary = models.FloatField(db_column='old_salary')
    salary = models.FloatField(db_column='new_salary')
    changeDate = models.DateField(db_column='changed_at')
    changedBy = models.CharField(max_length=100, db_column='changed_by')
    
    class Meta:
        db_table = 'salary_history'
        managed = False
    
    def __str__(self):
        return f"Salary history for {self.employeeId.firstName} {self.employeeId.lastName}"
    
#######################################################################################    

class Departments(models.Model):
    dept_id = models.IntegerField(primary_key=True, db_column='dept_id')
    name = models.CharField(max_length=100, db_column='dept_name')

    class Meta:
        db_table = 'departments'
        managed = False
        
    def __str__(self):
        return self.name

class Employees(models.Model):
    emp_id = models.IntegerField(primary_key=True, db_column='emp_id')
    department = models.ForeignKey(Departments, on_delete=models.DO_NOTHING, db_column='dept_id')
    first_name = models.CharField(max_length=50, db_column='first_name')
    last_name = models.CharField(max_length=50, db_column='last_name')
    email = models.EmailField()
    salary = models.IntegerField()

    class Meta:
        db_table = 'employees'
        managed = False    

class SalaryHistorys(models.Model):
    hist_id = models.IntegerField(primary_key=True, db_column='hist_id')
    employee = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, db_column='emp_id')
    old_salary = models.IntegerField(db_column='old_salary')
    new_salary = models.IntegerField(db_column='new_salary')
    changed_at = models.DateTimeField(db_column='changed_at')
    changed_by = models.CharField(max_length=50, db_column='changed_by')

    class Meta:
        db_table = 'salary_history'
        managed = False  
