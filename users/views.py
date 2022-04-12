from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as logthemin, logout as logthemout
from django.contrib import messages
from .forms import RegisterUserForm
from .models import Profile

def register(request):
	if request.user.is_authenticated:
		messages.success(request, 'You are logged in, log out first!')
		return redirect('home')
	else:
		if request.method == "POST":
			form = RegisterUserForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data['username']
				password = form.cleaned_data['password1']
				user = authenticate(username=username,password=password)
				logthemin(request, user)
				messages.success(request, 'Registration Successful')
				return redirect('home')
		else:
			form = RegisterUserForm()
		return render(request, 'users/register.html', {'form':form})


def login(request):
	if request.user.is_authenticated:
		messages.success(request, 'You are already logged in')
		return redirect('home')
	else:
		if request.method == "POST":
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				logthemin(request,user)
				return redirect('home')
			else:
				messages.success(request, 'Authentication error. Try again.')
				return redirect('login')
		else:
			return render(request, 'users/login.html', {})

def logout(request):
	logthemout(request)
	messages.success(request, 'Logged out.')
	return redirect('home')

def profile(request, uid):
	person = Profile.objects.get(user_id=uid)
	return render(request, 'users/profile.html', {'person':person})
