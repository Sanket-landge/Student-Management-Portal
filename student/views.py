from django.shortcuts import render, redirect
from student.models import Student
from student.forms import StudentForm


# Create your views here.
def displayRecords(request):
    students = Student.objects.all()
    return render(request,'student/dashboard.html',{'students':students})

def insertRecords(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'student/insert.html',{'form':form})

def updateRecords(request,id):
    student =  Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'student/update.html',{'student':student})

def deleteRecord(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')