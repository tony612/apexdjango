from django.conf.urls.defaults import *
from apexdjango.views import *
from apexdjango.users import views as users_views
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^apexdjango/', include('apexdjango.foo.urls')),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
	url(r'^$', pages_template, {'template_name': 'index.html', 'TITLE':'Home'}, name="Home"),
	url(r'^about', pages_template, {'template_name': 'about.html', 'TITLE':'About'}, name="About"),
	url(r'^store', pages_template, {'template_name': 'store.html', 'TITLE':'Store'}, name="Store"),
	url(r'^download', pages_template, {'template_name': 'download.html', 'TITLE':'Download'}, name="Download"),
	url(r'^support', pages_template, {'template_name': 'support.html', 'TITLE':'Support'}, name="Support"),
	url(r'^apps', pages_template, {'template_name': 'apps.html', 'TITLE':'Apps'}, name="Apps"),
	url(r'contact', pages_template, {'template_name': 'contact.html', 'TITLE':'Contact'}, name="Contact"),
	url(r'^signin', users_views.signin, {'template_name': 'signin.html', 'TITLE':'Sign In'}, name="Sign_In"),
	url(r'^signup', users_views.signup, {'template_name': 'signup.html', 'TITLE':'Sign Up'}, name="Sign_Up"),
	url(r'^logout', users_views.logout_view, name="Log_Out"),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
