from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	wallet = forms.CharField(required=True)
	password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma tu contrasena', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ("username", "email", "wallet", "password1", "password2")
		help_texts = {k:"" for k in fields}
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		# user.wallet = self.cleaned_data['wallet']
		if commit:
			user.save()
		return user