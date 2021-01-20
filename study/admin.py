from django.contrib import admin
from .models import Student, Course, CourseInstance, Professor, StudyGroup
from .forms import StudentForm
from ajax_select.admin import AjaxSelectAdmin
from import_export.admin import ImportExportModelAdmin

class StudentAdmin(AjaxSelectAdmin):
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
class CourseInstanceAdmin(ImportExportModelAdmin):
    list_display = ['course', 'course_title', 'section_number', 'call_number']

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass

