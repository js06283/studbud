from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
from django.http import HttpResponse
from .forms import StudentForm 
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def student_form(request):

    if request.method == 'POST': 
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_form')
    else: 
        form_class = StudentForm
        return render(request, 'form.html', {'form': form_class})
