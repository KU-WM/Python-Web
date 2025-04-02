from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True, db_column='dept_id', auto_created=True)
    name = models.CharField(max_length=100, blank=True, null=False, db_column='dept_name')
    parent = models.ForeignKey('self',null=True, blank=True, db_column='parent_id', on_delete=models.CASCADE, related_name='children')
    level = models.PositiveSmallIntegerField(db_column='dept_level')

    class Meta:
        managed = False
        db_table = 'dept_test'
        
    def __str__(self):
        return f"{self.id}: {self.name}"
    
class DepartmentTree(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', auto_created=True)
    master = models.CharField(max_length=100, blank=True, null=False, db_column='tree1')
    department = models.CharField(max_length=100, blank=True, null=False, db_column='tree2')
    team = models.CharField(max_length=100, blank=True, null=False, db_column='tree3')
    
    class Meta:
        managed = False
        db_table = 'dept_tree'
        
    def __str__(self):
        return f"{self.master}"