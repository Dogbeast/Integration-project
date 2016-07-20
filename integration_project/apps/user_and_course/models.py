from __future__ import unicode_literals

from ..login_and_registration.models import Users
from ..Courses.models import Course

from django.db import models
from django.contrib.auth import authenticate

# Create your models here.
class UserManager(models.Manager):
	def addCourseAndStudent(self, course, student):

		users_in_courses.userManager.create(User_in_Course=course, User_in_login=student)

	def sums(self):
		
		for student in course:
			print student.course

class users_in_courses(models.Model):
	# Class = models.CharField(max_length=50)
	# Student = models.CharField(max_length=100)
	User_in_Course = models.ForeignKey(Course)
	User_in_login = models.ForeignKey(Users)
	userManager = UserManager()