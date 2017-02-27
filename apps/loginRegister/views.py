from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse


def index(request):
	return render(request,'loginRegister/index.html')

def create_user(request):
	context = {
		'name' : request.POST["name"],
		'username' : request.POST["username"],
		'password' : request.POST["password"],
		'confirm_password' : request.POST["confirm_password"],
		'date': request.POST["date"],
	}

	if User.userManager.registration(context, request):
		passFlag = True
		user = User.objects.get(username = request.POST['username'])
		request.session['user_id'] = user.id
		request.session['user_name'] = user.name 
		return redirect(reverse('wishList:index'))
	else:
		passFlag = False
		return redirect(reverse('loginRegister:index'))
		


def login(request):
	content = {
	'username' : request.POST["username"],
	'password' : request.POST["password"],

	}
	if User.userManager.login(content, request):
		user = User.objects.get(username = request.POST['username'])
		request.session['user_name'] = user.name 
		print user.name
		request.session['user_id'] = user.id
		print user.id
		passFlag = True
		return redirect(reverse('wishList:index'))
	else:
		passFlag = False
		return redirect(reverse('loginRegister:index'))

def success(request):
	return redirect(reverse('wishList:index'), context)
    
def logout(request):
	request.session.flush()
	return redirect(reverse('loginRegister:index'))

 		



