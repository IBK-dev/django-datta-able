from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Societe,simpleUser
from .forms import Societe
 
# Create your views here.

def Societe_(request):
 if request.user.is_staff:
   societes=Societe.objects.all()
   context={'societes':societes}
   return render(request,'a-Société.html',context)
 else:
   soc=simpleUser.objects.get(user=request.user.id)
   societes=soc.societe.all()
   context={'societes':societes}

   
   return render(request,'a-Société.html',context)

def AffichageCard(request):
 if request.user.is_staff:
   societes=Societe.objects.all()
   context={'societes':societes}
   return render(request,'exercice/selectioneSocieteV2.html',context)
 else:
   soc=simpleUser.objects.get(user=request.user.id)
   societes=soc.societe.all()
   context={'societes':societes}
   return render(request,'exercice/selectioneSocieteV2.html',context)

def Creation_de_societe(request): 
    if request.method=='POST':
     if request.POST.get('raisonSocial'):
           savecord=Societe()
           savecord.raisonSocial = request.POST.get('raisonSocial')
           savecord.iff = request.POST.get('iff')
           savecord.ice = request.POST.get('ice')
           savecord.tp = request.POST.get('tp')
           savecord.rc = request.POST.get('rc')
           savecord.cnss = request.POST.get('cnss')
           savecord.formJuridique = request.POST.get('formJuridique')
           savecord.adress = request.POST.get('adress')
           savecord.model = request.POST.get('model')
           savecord.regime = request.POST.get('regime')
           savecord.commune = request.POST.get('commune')
           #savecord.profile_pic=request.FILES['logoSociete']
           savecord.save()
           messages.success(request,'creation succes...')
           return render(request,'a-Société.html')
    else:
      return render(request,'a-Société.html')  

def Visualiser_societe(request,pk):
  societes=Societe.objects.get(id=pk)
  context={'societes':societes}
  return render(request,'societe_editing.html',context)

def Edite_societe(request,pk):
   if request.method=='POST':
     if request.POST.get('raisonSocial'):
           societes=Societe.objects.get(id=pk)
           societes.raisonSocial = request.POST.get('raisonSocial')
           societes.iff = request.POST.get('iff')
           societes.ice = request.POST.get('ice')
           societes.tp = request.POST.get('tp')
           societes.rc = request.POST.get('rc')
           societes.cnss = request.POST.get('cnss')
           societes.formJuridique = request.POST.get('formJuridique')
           societes.adress = request.POST.get('adress')
           societes.model = request.POST.get('model')
           societes.regime = request.POST.get('regime')
           societes.commune = request.POST.get('commune')
           if len(request.FILES) !=0 :
              societes.profile_pic= request.FILES['logoSociete']
              societes.save()
           else:
               societes.save()
          
           context={'societes':societes}
           messages.success(request,'creation succes...')
           return render(request,'societe_editing.html',context) 
   else:
           return render(request,'societe_editing.html')     


def Delete_societe(request,pk):
  deletSociete=Societe.objects.get(id=pk)
  deletSociete.delete()
  societes=Societe.objects.all()
  context={'societes':societes}
  return render(request,'societe.html',context) 