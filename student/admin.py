# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Detail
from .models import Course
from .models import Subject


class StudentAdmin(admin.ModelAdmin):
	fieldset = [("Student Detail", {"field":["first_name","last_name"]})
	]
	
def Student_Course(self, obj):
	return obj.list_course()
	
	
class CourseAdmin(admin.ModelAdmin):
	list_display = ("course_name","course_description",)
	list_editable = ("course_description",)
	list_filter = ("course_name",)
	search_fields = ("course_name","course_description",)
	
class DetailAdmin(admin.ModelAdmin):
	list_display = ("first_name","middle_name","last_name",)
	list_editable = ("middle_name","last_name",)
	list_filter = ("last_name",)
	search_fields = ("first_name","last_name",)
	
class SubjectAdmin(admin.ModelAdmin):
	list_display = ("subject_name","subject_description",)
	list_editable = ("subject_description",)
	list_filter = ("subject_name",)
	search_fields = ("subject_name","subject_description",)

admin.site.register(Course,CourseAdmin)
admin.site.register(Detail,DetailAdmin)
admin.site.register(Subject,SubjectAdmin)



