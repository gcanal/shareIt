#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, date, timedelta
from django.contrib.auth import login,logout,authenticate                                                                         
from django.core.urlresolvers import reverse 
from django.contrib.auth.decorators import permission_required
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.utils import translation
#fromchaletDesAlpes.context_processors import view_name_context_processor
from django.template import RequestContext
from main.forms import SignInForm,SignUpForm

def home(request):
	return render(request, 'main/home.html')
"""	
def activate(request, lan,pageId):
	translation.activate(lan);
	return redirect(home)	
"""
