from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms
from django.utils.translation import ugettext_lazy as _

User._meta.local_fields[4].__dict__['_unique'] = True

GENDER_CHOICES = (
			('M', 'Male'),
			('F', 'Female'),
	)


class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True, verbose_name="expand_user")
	gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES, default='M')
	birthday = models.DateField('birthday', blank=True, null=True)
	homepage = models.URLField('homepage', blank=True)
	company = models.CharField('company', max_length=200, blank=True, null=True)
	conutry = models.CharField('country', max_length=50, blank=True, null=True)
	#def __unicode__(self):
	#	return u'%s %s' % (self.username, self.email)

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class RegisterForm(forms.Form):
	email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder':'Email'}))
	username = forms.RegexField(label='Username', regex=r'^[\w.@+-]+$',widget=forms.TextInput(attrs={'placeholder':'Username'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	pwconfirm = forms.CharField(label='Password Again', widget=forms.PasswordInput(attrs={'placeholder':'Password Confirm'}))

	def clean_email(self):
		emails = User.objects.filter(email=self.cleaned_data["email"])
		if not emails:
			return self.cleaned_data["email"]
		raise forms.ValidationError("Email existed!")

	def clean_pwconfirm(self):
		password1 = self.cleaned_data.get("password", "")
		password2 = self.cleaned_data["pwconfirm"]
		if password1 != password2:
			raise forms.ValidationError(_("The two password didn't match."))
		return password2
