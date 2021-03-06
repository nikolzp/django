from django.conf.urls import patterns, include, url
from django.contrib import admin, staticfiles
from pybursa.views import index, contact, student_list, student_detail
from pybursa import views

urlpatterns = patterns('',
	url(r'^$', index, name='index'),
	url(r'^contact/$', views.ContactView.as_view(), name='contact'),
	url(r'^student_list/$', student_list, name='student_list'),
	url(r'^student_detail/$', student_detail, name='student_detail'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
)
