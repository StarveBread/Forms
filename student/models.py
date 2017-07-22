# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Detail(models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	middle_name = models.CharField(max_length=150)
	age = models.IntegerField()
	b_day = models.DateTimeField()
	course = models.ManyToManyField("Course",related_name="Detail")
	
	
	def __str__(self):
		return "{} course {}".format(self.first_name,self.list_course())

	def list_course(self):
		return ",".join([course.course_name for course in self.course.all()])

	def save(self, *args,**kwargs):
		super(Detail,self).save(*args,**kwargs)




class Course(models.Model):
	course_name = models.CharField(max_length=150)
	course_description = models.TextField(max_length=550)
	subject = models.ManyToManyField("Subject",related_name="Courses")
	
	def __str__(self):
		return self.course_name
		
		
class Subject(models.Model):
	subject_name = models.CharField(max_length=150)
	subject_description = models.TextField(max_length=500)
	
	def __str__(self):
		return self.subject_name


