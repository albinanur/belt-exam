from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class UserManager(models.Manager):
	def registration(self, postData, request):
		passFlag = True
		if (not EMAIL_REGEX.match(postData['email'])):
			messages.warning(request, 'Email is not a valid email!')
			passFlag = False
		if (not postData['first_name'].isalpha()  or len(postData['first_name']) < 2):
			messages.warning(request, 'First_name is not  valid or too short!')
			passFlag = False
		if (len(postData['last_name']) < 2  or not postData['last_name'].isalpha()) :
			messages.warning(request, 'Last_name is not  valid or too short!')
			passFlag = False
		
		if len(postData['password']) < 8 :
			messages.warning(request, 'Password is too short!')
			passFlag = False
		if postData['confirm_password'] != postData['password']:
			messages.warning(request, 'Not match a password!')
			passFlag = False
		
		if passFlag == True: 
			messages.success(request, "Hello! Welcome, " + postData['first_name'] + "!")
			hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			User.objects.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = hashed)
		return passFlag


	def login(self, postData,request):
		passFlag = True
		if User.objects.filter(email = postData['email']):
			hashed = User.objects.get(email = postData['email']).password
			hashed = hashed.encode('utf-8')
			password = postData['password']
			password = password.encode('utf-8')
			if bcrypt.hashpw(password, hashed) == hashed:
				messages.success(request, "Success! Welcome, " + User.objects.get(email = postData['email']).first_name + "!")
				passFlag = True
			else:
				messages.warning(request, "Unsuccessful login. Incorrect password")
				passFlag = False
		else:
			messages.warning(request, "Unsuccessful login. Your email is incorrect.")
			passFlag = False
		return passFlag

	    
    
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length = 100, default='test@gmail.com')
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
    objects = models.Manager()
      