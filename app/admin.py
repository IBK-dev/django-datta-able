from  societ.models import Societe
from  exercices.models import Exercices
from encaissements.models import Encaissements
from deductions.models import Deductions
#from  societ.models import simpleUser

from django.contrib import admin
 
# Register your models here.
admin.site.register(Societe)
admin.site.register(Exercices)
admin.site.register(Encaissements)
admin.site.register(Deductions)
 
#admin.site.register(simpleUser)