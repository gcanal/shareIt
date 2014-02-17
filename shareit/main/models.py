#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
		
class Profil(models.Model):
	
    user = models.OneToOneField(User) # 1 profil pour un utilisateur
    #site_web = models.URLField(null=True, blank=True)
    email=models.EmailField(max_length=200);
    avatar=models.ImageField(upload_to='avatars/', verbose_name="Profil")
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    #l'adresse MEDIA_ROOT est concatene au champ upload_to
    #Pour manipulation des images installer python-imaging / PIL
    firstName=models.CharField(max_length=100)
    points=models.FloatField()
    nTokens=models.IntegerField();
    #signature = models.TextField(null=True, blank=True)
    #inscrit_newsletter = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u"Profil de {0}".format(self.user.username)


