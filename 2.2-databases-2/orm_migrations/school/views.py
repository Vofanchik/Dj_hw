from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    stu = Student.objects.all().order_by('group')
    # print(stu[3].teacher.all())
    context = {'object_list':stu}

    return render(request, template, context)