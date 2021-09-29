from django.core.checks import messages
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Exercices#, simpleUser
from societ.models import Societe

 
# Create your views here.



def periodescreation(request):
 
    if request.method=='POST':
     so=Societe.objects.filter(active=True).first()   
     print(so.id) 
     if request.POST.get('Nom'):
           savecord=Exercices()
           print("Hollo world")
           savecord.Nom = request.POST.get('Nom')
           savecord.Année = request.POST.get('Année')
           savecord.Prorata = request.POST.get('Prorata')
           savecord.model = request.POST.get('model')
           savecord.regime = request.POST.get('regime')
           savecord.societe_id = so.id
           savecord.save()
           messages.success(request,'creation succes...')
           periodes=Exercices.objects.filter(societe__active=True)
           context={'periodes':periodes}
           return render(request,'a-periodelist.html',context)
    periodes=Exercices.objects.filter(societe__active=True)
    context={'periodes':periodes}
    return render(request,'a-periodcreat.html',context)


def Edite_periode(request,pk):
      periodes=Exercices.objects.get(id=pk)
      if request.method=='POST':
          
           periodes.Nom = request.POST.get('Nom')
           print(request.POST.get('Année'))
           periodes.Année = request.POST.get('Année')
           periodes.Prorata = request.POST.get('Prorata')
           periodes.model = request.POST.get('model')
           periodes.regime = request.POST.get('regime')
           
           
           periodes.save()
          
           
           periodes=Exercices.objects.filter(societe__active=True)
           context={'periodes':periodes}
           messages.success(request,'creation succes...')
           return render(request,'a-periodelist.html',context)

      else:
            context={'periodes':periodes}
            messages.success(request,'creation succes...')
            return render(request,'a-periodedit.html',context)

def periodess(request):
    
      periodes=Exercices.objects.filter(societe__active=True)
      context={'periodes':periodes}
      return render(request,'a-periodelist.html',context)

     

     



def Delete_periode(request,pk):
  deletperiod=Exercices.objects.get(id=pk)
  deletperiod.delete()
  periodes=Exercices.objects.filter(societe__active=True)
  context={'periodes':periodes}
  return render(request,'a-periodelist.html',context) 
        
