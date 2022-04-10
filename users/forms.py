from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(label = '', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label='', max_length=50,widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm,self).__init__(*args, **kwargs)

		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
			self.fields[fieldname].label = ''
			self.fields[fieldname].widget.attrs['class']='form-control'

		self.fields['username'].widget.attrs['placeholder']='Username'
		self.fields['password1'].widget.attrs['placeholder']='Enter Password'
		self.fields['password2'].widget.attrs['placeholder']='Confirm Password'

