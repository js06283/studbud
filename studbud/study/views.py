from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
from django.http import HttpResponse
from .forms import StudentForm 
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def student_form(request):

    if request.method == 'POST': 
        form = StudentForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # uni = form.cleaned_data['uni']
            # email = form.cleaned_data['email']
            # new_student = form.save(commit=False)
            # new_student.uni = uni
            form.save()
            return redirect('student_form')
    else: 
        form_class = StudentForm
        return render(request, 'form.html', {'form': form_class})
