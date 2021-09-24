from django.db import models

# Create your models here.
class Student(models.Model):
    rollNo = models.IntegerField()
    name = models.CharField(max_length = 60)
    email = models.EmailField(max_length = 60)
    phoneNo = models.IntegerField()
    course = models.CharField(max_length = 60)


