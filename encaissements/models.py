from exercices.models import Exercices
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm,Textarea
from django.db import connections
#from  societ.models import Societe
#from  exercices.models import Exercices



# Create your models here.
class Encaissements(models.Model):
        
        Numéro_Facture = models.CharField(max_length=200)
        Date_Facture = models.CharField(max_length=200)
        Client = models.CharField(max_length=200)
        Nature = models.CharField(max_length=200)
        Référence = models.CharField(max_length=200)
        Code_TVA = models.CharField(max_length=200)
        Montant_HT = models.CharField(max_length=200)
        Montant_TVA = models.CharField(max_length=200)
        Montant_TTC = models.CharField(max_length=200)
        #societe=models.ForeignKey(Societe,null=True,on_delete=models.SET_NULL)
        #periode=models.ForeignKey(Exercices,null=True,on_delete=models.SET_NULL)
        

        #societe=models.ForeignKey(Societe,null=True,on_delete=models.SET_NULL)
        
class  Meta:
        db_table="encaissements"



        


#class simpleUser(models.Model):
#       user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
  #      societe = models.ManyToManyField(Societe)
#class  Meta:
 #       db_table="simpleUser"