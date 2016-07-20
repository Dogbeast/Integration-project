from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import authenticate
import bcrypt

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
	def process(self, first_name, last_name, email, password, confirm_password):
		if first_name.isalpha() and last_name.isalpha():
			if Users.userManager.existingUser(email):
				print "User already exists!"
				# return False
			elif len(first_name) < 2:
				print "first name less than 2"
			elif len(last_name) < 2:
				print "last name less than 2"
			elif password == confirm_password and Users.userManager.isValidEmail(email):
				pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())

				print "created new entry"
				Users.userManager.register(first_name, last_name, email, pw_hash)
				# return True
			else:
				print "failed to validate"
				# return False
		else:
			print "names not alpha!"

	def isValidEmail(self, email):
		if len(email) < 1:
			# flash("Email cannot be blank!")
			print "less than 1"
		elif not EMAIL_REGEX.match(email):
			# flash("email didn't work")
			print "didn't match"

		else:
			# flash("success!")
			return True
			print "match"

	def existingUser(self, email):
		if self.filter(email__exact=email):
			return True
		else:
			pass

	def ValidUser(self, email, password):

		person = self.filter(email__exact=email)
		if person:
			person = person[0]
		if person.password == bcrypt.hashpw(password.encode('utf-8'), person.password.encode('utf-8')):
			return True
		else:
			return False

		# pw = self.filter(email__exact=email)
		# if bwcrypt.hashpw(pw[1], )
		# if self.filter(email__exact=email) and self.filter(password__exact=password):
		print "before hash check"
		# pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
		# if self.filter(email__exact=email) and self.filter(password__exact=pw_hash):
		# 	print "after hash check"
		# 	return True

	def register(self, first_name, last_name, email, password):
		self.create(first_name=first_name, last_name=last_name, email=email, password=password)
		print "created new user"
		print first_name
		print last_name
		print email
		print password

class Users(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userManager = UserManager()