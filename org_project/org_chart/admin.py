from django.contrib import admin
from .models import Department, DepartmentTree


# Register your models here.
# admin.site.register(Department)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'level')
    list_filter = ('level',)
    search_fields = ('name',)
    ordering = ('id',)
    
@admin.register(DepartmentTree)
class DepartmentTreeAdmin(admin.ModelAdmin):
    list_display = ('master', 'department', 'team')
    list_filter = ('master',)
    search_fields = ('name',)
    ordering = ('master',)