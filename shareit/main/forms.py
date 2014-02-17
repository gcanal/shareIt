#-*- coding: utf-8 -*-
from django import forms

class SignUpForm(forms.Form):#s'enregister
	firstName=forms.CharField(label=(u"Prénom"),max_length=100,required=True);
	email=forms.EmailField(label=(u"Mail"));
	password=forms.CharField(label=(u"Mot de passe"), widget=forms.PasswordInput);
	#regles de validation
	def clean_password(self):
		motPasse=self.cleaned_data['password'];
		if len(motPasse)<6:
			raise forms.ValidationError((u"Le mot de Passe doit contenir au moins 6 caracteres"));
		return motPasse;
		
	def clean_email(self):
		mail=self.cleaned_data['email']
		if "@telecom-bretagne.eu" not in mail:
			raise forms.ValidationError((u"l'adresse mail doit finir en @telecom-bretagne.eu"))
		return mail
		
class SignInForm(forms.Form):# se connecter
	email=forms.EmailField(label=(u"Mail"));
	password=forms.CharField(label=(u"Mot de passe"), widget=forms.PasswordInput);
	#regles de validation
	def clean_password(self):
		motPasse=self.cleaned_data['password'];
		if len(motPasse)<6:
			raise forms.ValidationError((u"Le mot de Passe doit contenir au moins 6 caracteres"))
		return motPasse
		
	def clean_email(self):
		mail=self.cleaned_data['email']
		if "@telecom-bretagne.eu" not in mail:
			raise forms.ValidationError((u"l'adresse mail doit finir en @telecom-bretagne.eu"))
		return mail
	
		
class ProfilForm(forms.Form):
    firstName= forms.CharField(label=(u"Prénom"),max_length=100,)
    lastName=forms.CharField(label=(u"Nom"),max_length=100,)
    avatar= forms.ImageField(label=(u"Avater"),max_length=100,)
