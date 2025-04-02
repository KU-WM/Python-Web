from django.db import connection
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import DepartmentForm
from .models import Department, DepartmentTree
import oracledb
from collections import namedtuple

# connection = oracledb.connect(
#     user='hr',
#     password='tiger',
#     dsn='localhost/XEPDB1'          # 호스트명/서비스명
# )

# Create your views here.
def org_chart_view(request):
    roots = Department.objects.filter(level = 1)
    
    return render(request, 'org_chart/org_chart.html', {
        'departments': roots
    })

def departmentList(request):
    departments = DepartmentTree.objects.all()
    
    return render(request, 'org_chart/department_list.html', {
        'departments': departments
    })
    
def namedtuplefetchall(cursor):
    """Return all rows from a cursor as namedtuples"""
    desc = cursor.description
    nt_result = namedtuple('Row', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def department_list(request):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT dt1.DEPT_ID AS main_id, dt1.dept_name AS main_dept, dt2.DEPT_ID AS mid_id, dt2.dept_name AS mid_dept,
                dt3.DEPT_ID AS team_id, dt3.dept_name AS team
                FROM dept_test dt1
                LEFT JOIN dept_test dt2 ON dt1.dept_id = dt2.parent_id AND dt2.dept_level = 2
                LEFT JOIN dept_test dt3 ON dt2.dept_id = dt3.parent_id AND dt3.dept_level = 3
                WHERE dt1.dept_level = 1
                ORDER BY dt1.DEPT_NAME desc
        ''')

        rows = namedtuplefetchall(cursor)

    return render(request, 'org_chart/department_list.html', {'departments': rows})

def department_edit(request):
    department = Department.objects.get(id=request.GET.get('id'))
    
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return HttpResponse("<script type='text/javascript'>window.close(); window.opener.parent.location.reload();</script>")
    else:
        form = DepartmentForm(instance=department)
                
    return render(request, 'org_chart/change_data.html', {'form': form})