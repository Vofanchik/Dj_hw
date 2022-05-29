from django.contrib import admin

from .models import Student, Teacher

# class TeacherStudentInline(admin.TabularInline):
#     model = TeacherStudent

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
    # list_display = ['id', 'name', 'group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    # inlines = [TeacherStudentInline,]