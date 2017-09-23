# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.views.generic.detail import DetailView
from django.utils import timezone
from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import View, DetailView, UpdateView
from django.views.generic.edit import FormView

from .forms import StudentForm

from .models import Detail
from .models import Course
from .models import Subject
from .models import Faculty

# Create your views here.
def list_student(request):
		students = Detail.objects.exclude()
		context = {
		'students' : students,
		}
		return render(request,"index.html",context)
		

class StudentDetail(DetailView):
	model = Detail
	template_name = "student.html"


	
	def get_context_data(self, **kwargs):
		context = super(StudentDetail, self).get_context_data(**kwargs)
		return context

class courses_list(View):
	def get(self,request):
		courses = Course.objects.all()
		details = Detail.objects.all()
		context = {
		'courses' : courses,
		'details' : details,
		}
		return render(request,"courses.html",context)
		
class subjects_list(View):
	def get(self,request):
		subject = Subject.objects.all()
		context = {
		'subjects' : subject,
		}
		return render(request,"subjects.html",context)
		
class faculty_list(View):
	def get(self,request):
		faculties = Faculty.objects.all()
		context = {
		'faculty' : faculties,
		}
		return render(request,"Faculty.html",context)
		
		
class Student(View):
	def get(self, request):
		student = Detail.objects.all()
		context = {
			'student' : student,
			'form' : StudentForm,
		}
		return render(request, "student-form.html", context)
		
	def post(self, request):
		form = StudentForm(request.POST)
		student = Detail.objects.all()
		
		if form.is_valid():
			form.save()
			return redirect('student')
			
		context = {
			'form' : form,
			'student' : student,
		}
		
		return render(request, "student-form.html", context)
		
		
class StudentUpdate(UpdateView):
	model = Detail
	form_class = StudentForm
	template_name = 'student-form-edit.html'
	success_url = '#'
	

	def get_object(self, *args, **kwargs):
		first_name = get_object_or_404(Detail, pk=self.kwargs['pk'])

		
			
			
		return first_name
		

