from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt
import re



class UserManager(models.Manager):
	def registration(self, postData, request):
		passFlag = True
	
		if (not postData['name'].isalpha()  or len(postData['name']) < 3):
			messages.warning(request, 'Name is not  valid or too short!')
			passFlag = False
		if (len(postData['username']) < 3  or not postData['username'].isalpha()) :
			messages.warning(request, 'Last_name is not  valid or too short!')
			passFlag = False
		
		if not postData['password'].isalpha():
			messages.warning(request, 'Password should contain only characters!')
			passFlag = False
		if postData['confirm_password'] != postData['password']:
			messages.warning(request, 'Not match a password!')
			passFlag = False
		
		if passFlag == True: 
			messages.success(request, "Hello! Welcome, " + postData['name'] + "!")
			hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			User.objects.create(name = postData['name'], username = postData['username'], date = postData['date'],password = hashed)
		return passFlag


	def login(self, postData,request):
		passFlag = True
		if User.objects.filter(username = postData['username']):
			hashed = User.objects.get(username = postData['username']).password
			hashed = hashed.encode('utf-8')
			password = postData['password']
			password = password.encode('utf-8')
			if bcrypt.hashpw(password, hashed) == hashed:
				messages.success(request, "Success! Welcome, " + User.objects.get(username = postData['username']).name + "!")
				passFlag = True
			else:
				messages.warning(request, "Unsuccessful login. Incorrect password")
				passFlag = False
		else:
			messages.warning(request, "Unsuccessful login. Your Username is incorrect.")
			passFlag = False
		return passFlag

	    
    
class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    date  = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
    objects = models.Manager()
      