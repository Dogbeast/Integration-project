from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	# display current students in db
	context = {
	"courses": Course.objects.all()
	}
	print context
	return render(request, 'courses/index.html', context)

def add(request):
	# add new student to db
	Course.objects.create(course_name=request.POST['name'], description=request.POST['description'])
	# flash('Successfully entered, congratulations!')

	return redirect('/courses/')


def delete(request, id):
	# delete student from db
	context = {
		"course": Course.objects.get(id__exact=id)

	}

	return render(request, "courses/delete.html", context)

def destroy(request, id):
	
	Course.objects.filter(id=id).delete()

	return redirect('/courses/')

def deleteall(request):

	Course.objects.all().delete()

	return redirect ('/courses/')