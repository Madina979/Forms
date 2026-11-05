from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class SchoolClass(models.Model):
    name = models.CharField(max_length=20)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=30)

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

class Room(models.Model):
    number = models.IntegerField()
    floor = models.IntegerField()

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.IntegerField()
