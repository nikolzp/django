from django.shortcuts import render, redirect
from students.models import Student, CourseApplicetion
from courses.models import Course
from django import forms
from django.contrib import messages

class StudentApplyForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField(label="Mail", help_text='personal mail')
	package = forms.ChoiceField(choices=(('standeart', 'Standeart'), ('gold', 'Gold'), ('vip', 'Vip')), 
		widget=forms.RadioSelect, initial='standeart')
	new_subscribe = forms.BooleanField(required=False)


class CourseApplicationForm(forms.ModelForm):
	class Meta:
		model = CourseApplicetion
		exclude = ['comment', 'is_active']
		widgets = {'package':forms.RadioSelect}
		labels = {'email':"Mail"}
		help_texts = {'email': "Enter your Mail"}



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
		form = CourseApplicationForm(request.POST)
		if form.is_valid():
			application = form.save()
			messages.success(request, 'SAVED')
			return redirect('students:course-applicantion')
	else:
		form = CourseApplicationForm(initial={'news_subscribe':True})

	return render(request, 'students/apply.html', {'form':form})

def edit_application(request, pk):
	application = CourseApplicetion.objects.get(id=pk)
	if request.method == 'POST':
		form = CourseApplicationForm(request.POST, instance=application)
		if forom.is_valid():
			application = form.save()
			messages.success(request, 'SAVED')
			return redirect('students:course-applicantion')
	else:
		form = CourseApplicationForm(instance=application)

	return render(request, 'students/edit_application.html', {'form':form})

def delete_application(request, pk):
	application = CourseApplicetion.objects.get(id=pk)
	if request.method == 'POST':
		application.delete()
		messages.success(request, 'Deletetd')
		return redirect('students:course-applicantion')
	return render(request, 'students/delete_application.html')
