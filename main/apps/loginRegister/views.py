from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse


def index(request):
	return render(request,'loginRegister/index.html')

def create_user(request):
	context = {
		'email' : request.POST["email"],
		'first_name' : request.POST["first_name"],
		'last_name' : request.POST["last_name"],
		'password' : request.POST["password"],
		'confirm_password' : request.POST["confirm_password"],
	}

	if User.userManager.registration(context, request):
		passFlag = True
		user = User.objects.get(email = request.POST['email'])
		request.session['user_id'] = user.id
		request.session['user_first_name'] = user.first_name 
		return redirect(reverse('loginRegister:index'))
	else:
		passFlag = False
		return redirect(reverse('loginRegister:index'))
		


def login(request):
	content = {
	'email' : request.POST["email"],
	'password' : request.POST["password"],

	}
	if User.userManager.login(content, request):
		user = User.objects.get(email = request.POST['email'])
		request.session['user_first_name'] = user.first_name 
		print user.first_name
		request.session['user_id'] = user.id
		print user.id
		passFlag = True
		return redirect(reverse('loginRegister:index'))
	else:
		passFlag = False
		return redirect(reverse('loginRegister:index'))
def success(request):

	return redirect(reverse('loginRegister:index'), context)
	 

 		



