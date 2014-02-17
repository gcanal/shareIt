

from django.conf.urls import patterns, include, url
#from website.views import NouvelleWizard
#from website.forms import SectionForm, CalendarSetUpForm 


urlpatterns = patterns('main.views',
    url(r'^$', 'home'),
    #url(r'signIn^$', 'signIn'),#se connecter
     #url(r'signIn^$', 'signIn'), #s'enrgistrer
)
