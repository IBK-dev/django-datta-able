from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm,Textarea
#from django.contrib.auth.models import user
# Create your models here.
class Societe(models.Model):
        id = models.IntegerField(primary_key=True)
        raisonSocial=models.CharField(max_length=200)
        iff=models.CharField(max_length=200)
        ice=models.CharField(max_length=200)
        tp=models.CharField(max_length=200)
        rc=models.CharField(max_length=200)
        cnss=models.CharField(max_length=200)
        formJuridique=models.CharField(max_length=200)
        adress=models.CharField(max_length=200)
        model=models.CharField(max_length=200)
        regime=models.CharField(max_length=200)
        commune=models.CharField(max_length=200)
        profile_pic=models.ImageField(upload_to='soicetesLogos',null=True, blank=True)
class  Meta:
        db_table="societ"
class simpleUser (models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    societe=models.ManyToManyField(Societe)
    class  Meta:
        db_table="simpleUser"