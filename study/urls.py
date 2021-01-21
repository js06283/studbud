from django.urls import path
from . import views
# from .views import CourseAutocomplete #, UpdateView
from django.conf.urls import url
from django.urls import reverse

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.student_form, #UpdateView.as_view(),
        name='student_form'),
    path('confirm/', views.confirmation, name='confirmation')
    # url(
    #     r'course-autocomplete/$', 
    #     CourseAutocomplete.as_view(), 
    #     name = 'course-autocomplete',
    # ),
#     path('form/add/', views.student_add_form, name='student_add_form'),
 ]