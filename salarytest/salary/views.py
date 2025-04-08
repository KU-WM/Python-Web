from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Department, Employee, SalaryHistory
from .models import Departments, Employees, SalaryHistorys
from .forms import DepartmentFrom, EmployeeForm, SalaryHistoryForm
from django.db import connection, transaction
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# Create your views here.
def employeeList(request):
    employees = Employee.objects.all()
    return render(request, 'salary_list.html', {'employees': employees})

@csrf_exempt
def updateSalary(request, id):
    data = Employee.objects.get(id = id)
    if request.method == 'POST':
        with connection.cursor() as cursor:
            query = 'BEGIN proc_update_salary( p_emp_id => ' \
                    + request.POST.get('id') + ', p_new_salary => ' \
                    + request.POST.get('new_salary') + ', p_admin => ' \
                    + repr(request.POST.get('admin')) + '); END;/'
            cursor.execute(query)
        
        data = SalaryHistory.objects.filter(employeeId = request.POST.get('id'))
        form = Employee.objects.get(id = request.POST.get('id'))
        return render(request, 'salary_complete.html', {'form': form, 'datas':data})
        
    else:
        form = SalaryHistoryForm(instance=SalaryHistory)
    
    return render(request, 'salary_update.html', {'form': form, 'data': data})


###############################################################
# 1. 부서 드롭다운 보여주는 메인 페이지
def salary_update_view(requst):
    departments = Departments.objects.all()
    return render(requst, 'salary_update2.html', {'departments': departments})

# 2. 부서 ID에 따른 직원 리스트 (Ajax)
def get_employees(request):
    dept_id = request.GET.get('dept_id')
    employees = Employees.objects.filter(department = dept_id).values('emp_id', 'first_name', 'last_name', 'salary')
    return JsonResponse(list(employees), safe=False)


# 3. 직원 ID에 따른 급여 조회 (Ajax)
def get_salary(request):
    emp_id = request.GET.get('emp_id')
    emp = Employees.objects.get(emp_id=emp_id)
    return JsonResponse({'salary': emp.salary})

@csrf_exempt    
def update_salary(request):
    if request.method == "POST":
        emp_id = request.POST.get('emp_id')
        new_salary = int(request.POST.get('new_salary'))
        emp = Employees.objects.get(emp_id=emp_id)
    
        # 만일 급여 기록만 저장되고 변경에서 오류가 발생하여 데이터의 오류가 발생하는 경우를 방지하기 위해
        # 아래와 같이 transaction으로 묶어주면 내부 코드가 전부 처리된 후 한번에 commit 처리한다.
        with transaction.atomic():
            
            #급여 변경 기록
            SalaryHistorys.objects.create(
                hist_id=get_nextval('salary_hist_seq'),
                employee=emp,
                old_salary=emp.salary,
                new_salary=new_salary,
                changed_by='admin'
            )

            #급여 변경
            emp.salary = new_salary
            emp.save()

        return redirect('salary_complete', emp_id=emp.emp_id)
    
@csrf_exempt  
def update_salary_proc(request):
    if request.method == "POST":
        emp_id = request.POST.get('emp_id')
        new_salary = int(request.POST.get('new_salary'))
        admin_id = 'admin'
    
        try:
            with connection.cursor() as cursor:
                cursor.callproc('proc_update_salary', [emp_id, new_salary, admin_id])
                
        except Exception as e:
            print("프로시저 호출 오류 : ", e)
            return redirect(request, 'error.html', {'message': '급여 변경에 실패하였습니다.'})

        return redirect('salary_complete', emp_id=emp_id)

def salary_complete(request, emp_id):
    emp = Employees.objects.get(emp_id=emp_id)
    history = SalaryHistorys.objects.filter(employee=emp).order_by('-changed_at')
    return render(request, 'salary_complete2.html', {'emp':emp, 'history':history})

def get_nextval(sequence_name):
    with connection.cursor() as cursor:
        cursor.execute(f"select {sequence_name}.NEXTVAL FROM dual")
        row = cursor.fetchone()
        return row[0]
    
def employees(request):
    employees = Employees.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def deleteEmployees(request):
    emp_id = request.GET.get('emp_id')
    try:
        with connection.cursor() as cursor:
            cursor.callproc('proc_delete_employee', [emp_id])
            
    except Exception as e:
        print("프로시저 호출 오류 : ", e)
        return redirect(request, 'error.html', {'message': '급여 변경에 실패하였습니다.'})
    
    return redirect('employees')