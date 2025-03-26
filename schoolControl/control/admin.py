from django.contrib import admin
from .models import Student, Instructor, Lecture, Subject, Enrollment, Exam, Answer

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Lecture)
admin.site.register(Subject)
admin.site.register(Enrollment)
admin.site.register(Exam)
admin.site.register(Answer)