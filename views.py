from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
import settings

def custom_proc(request):
	return {
		'img_dir': settings.MEDIA_URL + 'images',
		'css_dir': settings.MEDIA_URL + 'stylesheets',
		'js_dir' : settings.MEDIA_URL + 'javascripts'
	}

def pages_template(request, template_name, TITLE):
	return render_to_response(template_name, {'TITLE': TITLE}, context_instance=RequestContext(request, processors=[custom_proc]))
