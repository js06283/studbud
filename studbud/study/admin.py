from django.contrib import admin
from .models import Student, Course, CourseInstance, Professor, StudyGroup
from .forms import StudentForm

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'uni', 'email']
    form = StudentForm
admin.site.register(Student, StudentAdmin)

@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ['group_num', 'course_instance']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_code']

@admin.register(CourseInstance)
class CourseInstanceAdmin(admin.ModelAdmin):
    list_display = ['course', 'section_number', 'call_number']

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass

