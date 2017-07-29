# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

from .models import Detail
from .models import Course

# Create your views here.
def list_student(request):
	students = Detail.objects.exclude()
	context = {
	'students' : students,
	}
	return render(request,"index.html",context)
	
class courses_list(View):
	def get(self,request):
		courses = Course.objects.all()
		context = {
		'courses' : courses,
		}
		return render(request,"courses.html",context)
		
class subjects_list(View):
	def get(self,request):
		subjects = Course.objects.all()
		context = {
		'subjects' : subjects,
		}
		return render(request,"subjects.html",context)
