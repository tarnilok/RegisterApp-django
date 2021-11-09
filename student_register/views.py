from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentInfo
from .forms import StudentForm
from django.core.paginator import Paginator
from django.contrib import messages

def home(request):
    return render(request, "student_register/home.html")

def student_list(request):
    students = StudentInfo.objects.all()
    student_paginator = Paginator(students, 5)
    page_num = request.GET.get('page')
    page = student_paginator.get_page(page_num)
    
    context = {
        "page" : page,
        "count" : student_paginator.count,
    }
    
    return render(request, "student_register/student_list.html", context)

def student_register(request):
    form = StudentForm()
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully")
            return redirect('list')
        else :
            messages.error(request, "Invalid form")
    context = {
        "form" : form
    }
    return render(request, 'student_register/student_register.html', context)
    
def student_detail(request, slug):
    student = get_object_or_404(StudentInfo, student_number=slug)
    context = {
        "student" : student
    }
    return render(request, "student_register/student_detail.html", context)
    

def student_edit(request, slug):
    student = get_object_or_404(StudentInfo, student_number=slug)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully")
            return redirect('list')
        else :
            messages.error(request, "Invalid form")
    context = {
        'student' : student,
        'form' : form,
    }  
    return render(request, 'student_register/student_edit.html', context)  

def student_delete(request, slug):
    student = get_object_or_404(StudentInfo, student_number=slug)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully")
        return redirect('list')
    context = {
        "student" : student
    }
    return render(request, 'student_register/student_delete.html', context)

