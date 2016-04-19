from django.db import models
from courses.models import Course

class Student(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	skype = models.CharField(max_length=255)
	courses = models.ManyToManyField(Course)

	def full_name(self):
		return self.name+" "+self.surname

		
class CourseApplicetion(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	courses = models.ForeignKey(Course)
	package = models.CharField(max_length=16, choices=(('standeart', 'Standeart'), ('gold', 'Gold'), ('vip', 'Vip')))
	new_subscribe = models.BooleanField()
	comment = models.TextField()
	is_active = models.BooleanField(default = True)
	
	def __unicode__(self):
		return self.name