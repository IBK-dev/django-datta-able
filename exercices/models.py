from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm,Textarea
from django.db import connections


# Create your models here.
class Exercices(models.Model):
        
        Nom = models.CharField(max_length=200)
        Année = models.CharField(max_length=200)
        Prorata = models.CharField(max_length=200)
        
class  Meta:
        db_table="exercices"




#class simpleUser(models.Model):
#       user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
  #      societe = models.ManyToManyField(Societe)
#class  Meta:
 #       db_table="simpleUser"