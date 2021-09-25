from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm,Textarea
from django.db import connections


# Create your models here.
class Societe(models.Model):
        id = models.IntegerField(primary_key=True)
        raisonSocial=models.CharField(max_length=200)
        iff=models.CharField(max_length=200)
        ice=models.CharField(max_length=200)
        tp=models.CharField(max_length=200)
        rc=models.CharField(max_length=200)
        cnss=models.CharField(max_length=200,null=True)
        formJuridique=models.CharField(max_length=200)
        adress=models.CharField(max_length=200)
        cni=models.CharField(max_length=200)
        tel=models.CharField(max_length=200)
        prenom=models.CharField(max_length=200)
        nom=models.CharField(max_length=200)
        ice=models.CharField(max_length=200)
        commune=models.CharField(max_length=200)
        #profile_pic=models.ImageField(upload_to='soicetesLogos',null=True, blank=True)
class  Meta:
        db_table="societ"


#class simpleUser(models.Model):
#       user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
  #      societe = models.ManyToManyField(Societe)
#class  Meta:
 #       db_table="simpleUser"