from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    students = Student.objects.all()
    return render(request, 'school/students.html', {'students': students, 'form': form})

def courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    courses = Course.objects.all()
    return render(request, 'school/courses.html', {'courses': courses, 'form': form})

def details(request, student_id):
    student = Student.objects.get(pk=student_id)
    not_registered_courses = Course.objects.exclude(students=student)
    return render(request, 'school/details.html', {'student': student, 'not_registered_courses': not_registered_courses})
