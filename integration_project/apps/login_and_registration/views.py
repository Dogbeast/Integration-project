from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):

	return render(request, 'login_and_registration/index.html')

# def process(request):
# 	if Users.userManager.existingUser(request.POST['email']):
# 		print "User already exists!"
# 		return redirect('/')
# 	elif request.POST['password'] == request.POST['confirm_password'] and Users.userManager.isValidEmail(request.POST['email']):
# 		print "created new entry"
# 		Users.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'])
# 		return redirect('/')
# 	else:
# 		print "failed to validate"
# 		return redirect('/')

def process(request):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	password = request.POST['password'].encode('utf-8')
	confirm_password = request.POST['confirm_password']
	Users.userManager.process(first_name, last_name, email, password, confirm_password)

	return redirect('/login_and_registration/')

def login(request):
	if Users.userManager.ValidUser(request.POST['email'], request.POST['password'].encode('utf-8')):
		return redirect('/login_and_registration/success')
	else:
		print "No users"
		return redirect('/login_and_registration/')

def success(request):
	context = {
		'users':Users.userManager.all()
	}
	print context
	return render(request, 'login_and_registration/success.html', context)

def delete(request):

	Users.userManager.all().delete()

	return redirect ('/login_and_registration/')