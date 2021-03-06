from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
	url(r'^$', views.StudentListView.as_view(), name='list_view'),
	url(r'^(?P<pk>\d+)/', views.StudentDetailView.as_view(), name='detail'),
	url(r'^add/$', views.create, name='add'),
	url(r'^edit/(?P<student_id>\d+)/$', views.edit, name='edit'),
	url(r'^remove/(?P<student_id>\d+)/$', views.remove, name='remove'),

)