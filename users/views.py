from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from apexdjango.users.models import UserProfile, RegisterForm
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from apexdjango import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import 	login_required

def custom_proc(request):
	return {
		'img_dir': settings.MEDIA_URL + 'images',
		'css_dir': settings.MEDIA_URL + 'stylesheets',
		'js_dir' : settings.MEDIA_URL + 'javascripts'
	}

def signin(request, template_name, TITLE):
	if request.method == 'GET':
		# keep url from
		request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
		#return HttpResponse('get method')
		return render_to_response(template_name, {'TITLE': TITLE}, context_instance=RequestContext(request, processors=[custom_proc]))
	elif request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				# redirect to previouce page
				return HttpResponseRedirect(request.session['login_from'])
				#return HttpResponse('success')
			else:
				return HttpResponse('User is not active')
		else:
			return HttpResponse('The email and the password can\'t match')

def logout_view(request):
	logout(request)
	#return render_to_response('index.html', {'TITLE':'Home'}, context_instance=RequestContext(request, processors=[custom_proc]))
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def signup(request, template_name, TITLE):
	if request.method == 'POST':
		form = RegisterForm(request.POST.copy())
		if form.is_valid():
			username = form.cleaned_data["username"]
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			new_user = User.objects.create_user(username, email, password)
			new_user.backend='django.contrib.auth.backends.ModelBackend'
			login(request, new_user)
			return render_to_response('index.html', {'TITLE': 'Home'}, context_instance=RequestContext(request, processors=[custom_proc]))
	elif request.method == 'GET':
		form = RegisterForm()
	#	return HttpResponse('signup')
	return render_to_response(template_name, {'TITLE': TITLE, 'form':form}, context_instance=RequestContext(request, processors=[custom_proc]))

def showall(request, template_name, TITLE, user_list):
	return render_to_response(template_name, {'TITLE':TITLE, 'user_list':user_list}, context_instance=RequestContext(request, processors=[custom_proc]))

@login_required
def profile(request, template_name, TITLE):
	return render_to_response(template_name, {'TITLE':TITLE}, context_instance=RequestContext(request, processors=[custom_proc]))

