from django.shortcuts import render, redirect
from ..login_and_registration.models import Users
from ..Courses.models import Course

from .models import users_in_courses

# Create your views here.


def index(request):
	newList = users_in_courses.userManager.all()

	courses = Course.objects.all()

	users = Users.userManager.all()

	# sums = users_in_courses.userManager.filter()
	# print "SUMS HERE:"
	# print users_in_courses.userManager.sums()
	print courses[0]
	print newList[0]
	MathCount = 0
	EnglishCount = 0
	CSSCount = 0
	for x in newList:
		if x.User_in_Course.course_name == "Math":
			MathCount +=1
		if x.User_in_Course.course_name == "English":
			EnglishCount +=1
		if x.User_in_Course.course_name == "CSS":
			CSSCount +=1
	print MathCount
	print EnglishCount
	print CSSCount

	context = {
		"users": users,
		"courses": courses,
		"newList": newList,
		"MathCount": MathCount,
		"EnglishCount": EnglishCount,
		"CSSCount": CSSCount
	}
	# print context

	return render(request, 'user_and_course/index.html', context)

def login_page(request):
	pass

def add_course_and_student(request):
	print "Test"
	print request.POST['courseName']
	print "xxxxxxxxxxxx"
	print request.POST['firstNameLastName']

	course = Course.objects.get(id__exact=request.POST['courseName'])
	print course
	student = Users.userManager.get(id__exact=request.POST['firstNameLastName'])
	print student
	users_in_courses.userManager.addCourseAndStudent(course, student)

	return redirect('/user_and_course/')

def deleteNewListUser(request, id):

	users_in_courses.userManager.get(id=id).delete()
	return redirect ('/user_and_course/')