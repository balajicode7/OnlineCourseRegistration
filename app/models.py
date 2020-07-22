from django.db import models

# Create your models here.
class Schedule_Class(models.Model):
    idno=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=30)
    faculty=models.CharField(max_length=30)
    date=models.DateField()
    time=models.TimeField()
    fee=models.IntegerField(max_length=10)
    duration=models.IntegerField(max_length=5)


class Student_Registration(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contactno=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    password=models.IntegerField(max_length=20)
