from django.shortcuts import render, redirect
from .models import Student, Instructor
from .forms import StudentFrom, InstructorForm

def userList(request):
    students = Student.objects.all()
    return render(request, 'control/userlist.html', {'students': students})

def userLogin(request):
    if request.method == 'POST':
        form = request.POST
        print("TEST:======================\n",form['name'], form['Email'], form['Password'], form['type'])
        if form['type'] == "pro":
            data = Instructor.objects.filter(email=form['Email'] , password=form['Password'])
        else:
            data = Student.objects.filter(Email=form['Email'] , Password=form['Password'])
        if data:
            print("Login Success!")
            print(data)
            return redirect('login')
        else:
            print(data)
            return redirect('/admin')
    else:
        form = StudentFrom()
    return render(request, 'control/login.html', {'form': form})