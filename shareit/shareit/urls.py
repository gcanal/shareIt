from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #gestion des fichiers statiques en developpement
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings 
from django.conf.urls.i18n import i18n_patterns
admin.autodiscover()


admin.autodiscover()
urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),#not  within i18n_patterns() - it needs to be language-independent 
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += i18n_patterns('',
    url(r'^accueil/$', 'main.views.home'),
    url(r'^$', 'main.views.home'),
    url(r'^main/', include('main.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', #vraiment faire une enquete la dessus
                 {'document_root': settings.MEDIA_ROOT}),   
)

urlpatterns += staticfiles_urlpatterns() ######## Modifie pour developpement
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #pour les images durant le developpement

