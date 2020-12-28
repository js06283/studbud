from django.contrib import admin
from .models import Student, Course, CourseInstance, Professor

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'uni', 'email']
admin.site.register(Student, StudentAdmin)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseInstance)
class CourseInstanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass

