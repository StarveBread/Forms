"""form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from student.views import subjects_list,courses_list,list_student,faculty_list, StudentDetail,Student,StudentUpdate

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^student/$', list_student,name='student'),
	url(r'^student/(?P<pk>[-\w]+)/$',StudentDetail.as_view(),name='studentdetail'),
	url(r'^student-form/$', Student.as_view(), name='student-form'),
	url(r'^student/(?P<pk>[-\w]+)/edit/$', StudentUpdate.as_view(), name='student-form-edit'),
	url(r'^courses/$',courses_list.as_view(),name="courses"),
	url(r'^subjects/$',subjects_list.as_view(),name="subjects"),
	url(r'^faculty/$',faculty_list.as_view(),name="faculty"),
]
