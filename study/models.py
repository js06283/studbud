from django.db import models
import uuid
from django.forms import ModelForm
import pytz

TIME_MANAGEMENT_CHOICES = [
    (1, 'Finish far before the deadline (days before the deadline)'),
    (2, 'Finish early (a day or two before the deadline)'),
    (3, 'Finish with a little bit of time left over (several hours before the deadline)'),
    (4, 'Finish at the last minute (several minutes before deadline)')
]
COLLABORATIVE_CHOICES = [
    (1, '1 Prefer minimal talking'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5 Very interactive')
]
SERIOUSNESS_CHOICES = [
    (1, '1 Not so serious'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5 Very serious student')
]
EXTROVERTED_CHOICES = [
    (1, '1 Not extroverted'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5 Very extroverted')
]
TIME_ZONE_CHOICES = [
    (1, 'UTC -4 through UTC -5 AKA Eastern (EST) or Central (CST)'),
    (2, 'UTC -6 through UTC -7 AKA Mountain (MST) or Pacific (PST)'),
    (3, 'UTC -8 through UTC -12 or UTC +12 through UTC +9'),
    (4, 'UTC +8 through UTC -3')
]
DISCOVERY_CHOICES = [
    ('class', 'Class'),
    ('discord', 'Discord'),
    ('facebook', 'Facebook'),
    ('friend', 'Friend'),
    ('groupme', 'GroupMe'),
    ('instagram', 'Instagram'),
    ('slack', 'Slack'),
    ('snapchat', 'Snapchat'),
    ('student_council', 'Student Council')
]
SEMESTER_CHOICES = [
    ('spring_2021','Spring 2021'),
    ('summer_2021', 'Summer 2021')
]

class Student(models.Model):
    """Model representing a student."""
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    uni = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 50)
    phone = models.CharField(max_length = 15, null = True, default = '0000000000')
    timezone = models.CharField("Timezone", max_length=128, choices = TIME_ZONE_CHOICES)
                   #choices=[(tz, tz) for tz in pytz.all_timezones], default = 'America/New_York')
    time_management = models.IntegerField(default = 0, choices = TIME_MANAGEMENT_CHOICES)
    collaborative = models.IntegerField(default = 0, choices = COLLABORATIVE_CHOICES)
    academic_seriousness = models.IntegerField(default = 0, choices = SERIOUSNESS_CHOICES)
    extroverted = models.IntegerField(default = 0, choices = EXTROVERTED_CHOICES)
    discovery = models.CharField(max_length = 50, choices = DISCOVERY_CHOICES)
    fun_facts = models.CharField(max_length = 100, null = True)
    courses= models.ManyToManyField('CourseInstance')

    def __str__(self):
        return self.uni

class StudyGroup(models.Model):
    """Model representing a study group"""
    group_num = models.CharField(max_length = 10, default = "0000")
    students = models.ManyToManyField('Student')
    course_instance = models.ForeignKey('CourseInstance', on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.group_num

class Course(models.Model):
    """Model representing a course"""
    name = models.CharField(max_length = 100, null = True)
    course_code = models.CharField(max_length = 10, default = "00000")
    
    def __str__(self):
        return self.course_code 

class CourseInstance(models.Model):
    """Model representing a course instance"""
    #course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    course = models.CharField(max_length = 50, default = '')
    section_number = models.CharField(max_length = 3, default = "000")
    call_number = models.CharField(max_length = 10, default = "00000")
    #professor = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True)
    professor = models.CharField(max_length = 50, default = '')
    #location = models.CharField(max_length = 50, null = True)
    num_students = models.IntegerField(null = True)
    time = models.CharField(max_length = 50, null = True)
    #semester = models.CharField(max_length = 50, choices = SEMESTER_CHOICES, default = "")
    semester = models.CharField(max_length = 50, default = '')
    course_title = models.CharField(max_length = 50, default = '')
    course_name = models.CharField(max_length = 150, default = 'null')
    course_query = models.CharField(max_length = 250, default = 'null')

    def save(self, *args, **kwargs):
        self.course_name = str(self.course) + ' ' + str(self.course_title)  +  ' ' + self.time + ' (' + self.call_number + ')'
        self.course_query = str(self.course) + ' ' + str(self.course_title) + ' sec: ' + self.section_number + ' ' + self.time + ' ' + self.professor + ' ' + self.call_number 
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.course) + ' ' + str(self.course_title)  + ' ' + self.time
        
class Professor(models.Model):
    """Model representing a professor"""
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name 
