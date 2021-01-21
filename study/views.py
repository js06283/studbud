from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
from django.http import HttpResponse
# Version with working http
from .forms import StudentForm #StudentAddForm
from django.urls import reverse
# from dal import autocomplete
from study.models import CourseInstance
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'index.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def student_form(request):

    if request.method == 'POST': 
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/study/confirm/')
    else:
        form = StudentForm
    context = {'form': form}

    return render(request, 'form.html', context)

# class CourseAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         qs = CourseInstance.objects.all()

#         if self.q:
#             qs = qs.filter(course_name__istartswith=self.q)
#             # qs = qs.filter(reason__icontains=self.q)

#         return qs

# class StudentCreate(CreateView):
#     model = student

# class UpdateView(generic.UpdateView):
#     model = CourseInstance
#     form_class = StudentForm
#     template_name = 'form.html'
#     success_url = reverse_lazy('student-form')
#     formset_class = modelformset_factory(
#         CourseInstance,
#         form=StudentForm,
#         extra=1,
#         # fk_name='for_inline',
#         fields=('first_name', 'last_name', 'uni', 'email', 'phone','time_zone', 'time_management',
#                      'collaborative', 'academic_seriousness', 'extroverted', 'discovery','fun_facts','course_instances')
#     )

#     def get_object(self):
#         return CourseInstance.objects.first()

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()

#         form = self.get_form()
#         if form.is_valid() and self.formset.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         result = super().form_valid(form)
#         self.formset.save()
#         return result

#     @property
#     def formset(self):
#         if '_formset' not in self.__dict__:
#             setattr(self, '_formset', self.formset_class(
#                 self.request.POST if self.request.method == 'POST' else None,
#                 instance=getattr(self, 'object', self.get_object()),
#             ))
#         return self.formset

# def student_add_form(request):
#     student = get_object_or_404(Customer, pk=uni)
#     form = StudentAddForm(request.POST)
#     if form.is_valid():
#         student = form.save(commit=False)
#         student.uni=student.uni
#         student.course_instances=student.course_instances
