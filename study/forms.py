from django import forms
from .models import Student, CourseInstance
from django.forms import ModelForm
import pytz
from django.utils.safestring import mark_safe
from django.forms.widgets import RadioSelect, Textarea
# from dal import autocomplete
from django.utils.html import format_html
from ajax_select.fields import AutoCompleteSelectMultipleField
from ajax_select import make_ajax_field
from django.forms import widgets


#THIS CLASS ISN'T WORKING -- horizontal radio buttons. also be sure to change the widget type for the different options in StudentForm class
# class HorizontalRadioRenderer(forms.RadioSelect):
#     def render(self, name, value, attrs=None, renderer=None):
#         return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

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

# class CourseAutocomplete(autocomplete.Select2QuerySetView):
#     def get_result_label(self, item):
#         return format_html('<img src="flags/{}.png"> {}', item.name, item.name)

class StudentForm(ModelForm):
    first_name = forms.CharField(label= 'First Name ', widget=forms.TextInput)
    last_name = forms.CharField(label = 'Last Name ', widget=forms.TextInput)
    uni = forms.CharField(label = 'UNI ', widget=forms.TextInput, error_messages={'unique': 'Student with this UNI already exists, if this is a mistake or you would like to add more courses, please email studbud.columbia@gmail.com.'})
    email = forms.EmailField(label = 'Email ', widget=forms.TextInput, error_messages={'unique': 'Student with this email already exists, if this is a mistake or you would like to add more courses, please email studbud.columbia@gmail.com.'})
    phone = forms.CharField(label = 'Phone number')

    timezone = forms.ChoiceField(
        choices = TIME_ZONE_CHOICES, 
        label = 'Time zone ',
        widget = forms.RadioSelect)
    time_management = forms.ChoiceField(
        choices = TIME_MANAGEMENT_CHOICES, 
        initial = 0, 
        widget = forms.RadioSelect(attrs={'display': 'inline-block',}), 
        label = 'How do you manage your time for assignments?')
    collaborative = forms.ChoiceField(
        choices = COLLABORATIVE_CHOICES, 
        widget=forms.RadioSelect, 
        label = 'How collaborative are you?')
    academic_seriousness = forms.ChoiceField(
        choices = SERIOUSNESS_CHOICES, 
        widget = forms.RadioSelect, 
        label = 'How serious of a student are you?')
    extroverted = forms.ChoiceField(
        choices = EXTROVERTED_CHOICES, 
        widget = forms.RadioSelect, 
        label = 'How extroverted are you?')
    discovery = forms.ChoiceField(choices = DISCOVERY_CHOICES, 
        widget = forms.RadioSelect)
    fun_facts = forms.CharField(widget=Textarea(attrs={"rows":3, "cols":30}), 
       label='Enter one fun fact about yourself! This will be shared with your group(s)')
    courses = AutoCompleteSelectMultipleField('courses', 
        label = 'Courses (enter at least 3 characters of your professor, course name, or call number to search)',
        help_text='Searching for your course will initiate a dropdown menu of courses to select from. Be sure to find the correct section number for your course if there are multiple. You may select multiple courses, so please add all courses you would like a study group for before submitting.')
    
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'uni', 'email', 'phone','timezone', 'time_management',
                     'collaborative', 'academic_seriousness', 'extroverted', 'discovery','fun_facts','courses']
    
    
# class StudentAddForm(ModelForm):
#     uni = forms.CharField(label = 'UNI')
#     course_instances = forms.MultipleChoiceField(queryset = CourseInstance.objects.all())

#     class Meta:
#         model = Student
#         fields = ['uni', 'course_instances']