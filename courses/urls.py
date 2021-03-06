from django.conf.urls import patterns, include, url
from courses import views

urlpatterns = patterns('',
	url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
	url(r'^add/$', views.add, name='add'),
	url(r'^edit/(?P<course_id>\d+)/$', views.edit, name='edit'),
	url(r'^remove/(?P<course_id>\d+)/$', views.remove, name='remove'),
	url(r'^(?P<course_id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
)