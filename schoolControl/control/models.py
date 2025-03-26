from django.db import models

class Student(models.Model):
    StudentID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Student'
        
    def __str__(self):
        return f"{self.StudentID}: {self.name}"

class Instructor(models.Model):
    InstructorID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Instructor'

class Subject(models.Model):
    SubjectID = models.IntegerField(primary_key=True)
    SubjectName = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Subject'

class Lecture(models.Model):
    LectureID = models.IntegerField(primary_key=True)
    SubjectID = models.ForeignKey(Subject, on_delete=models.CASCADE, db_column='SubjectID')
    InstructorID = models.ForeignKey(Instructor, on_delete=models.CASCADE, db_column='InstructorID')
    LectureName = models.CharField(max_length=100)
    StartDate = models.DateField()
    EndDate = models.DateField()

    class Meta:
        managed = False
        db_table = 'Lecture'

class Enrollment(models.Model):
    EnrollmentID = models.IntegerField(primary_key=True)
    LectureID = models.ForeignKey(Lecture, on_delete=models.CASCADE, db_column='LectureID')
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='StudentID')
    StartDate = models.DateField()
    EndDate = models.DateField()

    class Meta:
        managed = False
        db_table = 'Enrollment'

class Exam(models.Model):
    ExamID = models.IntegerField(primary_key=True)
    LectureID = models.ForeignKey(Lecture, on_delete=models.CASCADE, db_column='LectureID')
    ExamContent = models.TextField()
    StartDate = models.DateField()
    EndDate = models.DateField()

    class Meta:
        managed = False
        db_table = 'Exam'

class Answer(models.Model):
    AnswerID = models.IntegerField(primary_key=True)
    ExamID = models.ForeignKey(Exam, on_delete=models.CASCADE, db_column='ExamID')
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE, db_column='StudentID')
    AnswerContent = models.TextField()
    colabUrl = models.URLField()
    score = models.IntegerField()
    feedback = models.TextField()

    class Meta:
        managed = False
        db_table = 'Answer'

