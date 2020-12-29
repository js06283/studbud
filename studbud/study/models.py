from django.db import models
import uuid
from django.forms import ModelForm
import pytz

# Create your models here.

class Student(models.Model):
    """Model representing a student."""
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    uni = models.CharField(max_length = 10)
    email = models.CharField(max_length = 50)
    timezone = models.CharField("Timezone", max_length=128, 
                   choices=[(tz, tz) for tz in pytz.all_timezones], default = 'America/New_York')
    time_management = models.IntegerField()

    def __str__(self):
        """String for representing the student"""
        return self.uni

class Course(models.Model):
    name = models.CharField(max_length = 100)
    course_code = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.course_code 

class CourseInstance(models.Model):
    call_number = models.CharField(max_length = 10)
    professor = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.call_number

class Professor(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name 
