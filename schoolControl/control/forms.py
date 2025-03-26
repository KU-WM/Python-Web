from django import forms
from .models import Student, Instructor

class StudentFrom(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'Email', 'Password']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'email', 'password']