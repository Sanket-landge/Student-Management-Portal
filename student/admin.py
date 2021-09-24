from django.contrib import admin
from student.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollNo','name','email','phoneNo','course']

admin.site.register(Student,StudentAdmin)
