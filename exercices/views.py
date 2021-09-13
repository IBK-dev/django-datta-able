from django.core.checks import messages
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Exercices#, simpleUser

 
# Create your views here.

def periodess(request):
     if request.user.is_staff:
      periodes=Exercices.objects.all()
      context={'periodes':periodes}
      return render(request,'a-periodelist.html',context)

     else:
       per=simpleUser.objects.get(user=request.user.id)
       periodes=per.periodes.all()
       context={'periodes':periodes}

     return render(request,'a-periodelist.html',context)

def periodescreation(request):
 
    if request.method=='POST':
     if request.POST.get('Nom'):
           savecord=Exercices()
           print("Hollo world")
           savecord.Nom = request.POST.get('Nom')
           savecord.Année = request.POST.get('Année')
           savecord.Prorata = request.POST.get('Prorata')
           
           savecord.save()
           messages.success(request,'creation succes...')
           periodes=Exercices.objects.all()
           context={'periodes':periodes}
           return render(request,'a-periodelist.html',context)
    periodes=Exercices.objects.all()
    context={'periodes':periodes}
    return render(request,'a-periodcreat.html',context)
        
