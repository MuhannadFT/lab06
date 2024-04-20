from django.forms import ModelForm
from .models import Student, Course

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
