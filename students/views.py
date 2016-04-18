from django.shortcuts import render, redirect
from students.models import Student, CourseApplicetion
from courses.models import Course
from django import forms

class StudentApplyForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField(label="Mail", help_text='personal mail')
	package = forms.ChoiceField(choices=(('standeart', 'Standeart'), ('gold', 'Gold'), ('vip', 'Vip')), 
		widget=forms.RadioSelect, initial='standeart')
	new_subscribe = forms.BooleanField(required=False)



def list_view(request):
	if request.GET:
		deskr = Student.objects.filter(courses__id=int(request.GET['course_id']))
	else:
		deskr = Student.objects.all()
	return render(request, 'students/list.html', {'deskr':deskr})


def detail(request, student_id):
	det = Student.objects.get(id=student_id)
	return render(request, 'students/detail.html', {'det':det})

def apply_to_course(request):
	if request.method == 'POST':
		form = StudentApplyForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			application = CourseApplicetion()
			application.name = data['name']
			application.email = data['email']
			application.package = data['package']
			application.new_subscribe = data['new_subscribe']
			course = Course.objects.get(id=1)
			application.courses = course
			application.save()
			return redirect('students:course-applicantion')
	else:
		form = StudentApplyForm(initial={'news_subscribe':True})

	return render(request, 'students/apply.html', {'form':form})