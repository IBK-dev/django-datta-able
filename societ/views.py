from django.core.checks import messages
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Societe#, simpleUser

 
# Create your views here.


def Creation_de_societe(request):
 
    if request.method=='POST':
     if request.POST.get('raisonSocial'):
           savecord=Societe()
           print("Hollo world")
           savecord.raisonSocial = request.POST.get('raisonSocial')
           savecord.iff = request.POST.get('iff')
           savecord.ice = request.POST.get('ice')
           savecord.tp = request.POST.get('tp')
           savecord.rc = request.POST.get('rc')
           savecord.cnss = request.POST.get('cnss')
           savecord.formJuridique = request.POST.get('formJuridique')
           savecord.adress = request.POST.get('adress')
           savecord.prenom = request.POST.get('prenom')
           savecord.nom = request.POST.get('nom')
           savecord.tel = request.POST.get('tel')
           savecord.cni = request.POST.get('cni')
           #savecord.profile_pic=request.FILES['logoSociete']
           savecord.save()
           messages.success(request,'creation succes...')
           societes=Societe.objects.all()
           context={'societes':societes}
           return render(request,'a-societelist.html',context)
          
    else:
          print("Hollo world")
    societes=Societe.objects.all()
    context={'societes':societes}
    return render(request,'a-société.html',context)
        
def Edite_societe(request,pk):
      societes=Societe.objects.get(id=pk)
      if request.method=='POST':
          if request.POST.get('raisonSocial'):
           
           societes.raisonSocial = request.POST.get('raisonSocial')
           societes.iff = request.POST.get('iff')
           societes.ice = request.POST.get('ice')
           societes.tp = request.POST.get('tp')
           societes.rc = request.POST.get('rc')
           societes.cnss = request.POST.get('cnss')
           societes.formJuridique = request.POST.get('formJuridique')
           societes.adress = request.POST.get('adress')
           societes.nom = request.POST.get('nom')
           societes.prenom = request.POST.get('prenom')
           societes.tel = request.POST.get('tel')
           societes.cni = request.POST.get('cni')
           
           societes.save()
          
           context={'societes':societes}
           messages.success(request,'creation succes...')
           return render(request,'a-societe_editing.html',context)
      else:
           context={'societes':societes}
           messages.success(request,'creation succes...')
           return render(request,'a-societe_editing.html',context)
   

def AffichageCard(request):
      if request.user.is_staff:
            societes=Societe.objects.all()
            context={'societes':societes}
            return render(request,'a-societelist.html',context)

      else:
                  soc=simpleUser.objects.get(user=request.user.id)
                  societes=soc.societe.all()
                  context={'societes':societes}
                  return render(request,'a-societelist.html',context)


def societe(request):
 if request.user.is_staff:
   societes=Societe.objects.all()
   context={'societes':societes}
   return render(request,'a-societelist.html',context)
 else:
   soc=simpleUser.objects.get(user=request.user.id)
   societes=soc.societe.all()
   context={'societes':societes}

   
   return render(request,'a-societelist.html',context)



def Visualiser_societe(request,pk):
  societes=Societe.objects.get(id=pk)
  context={'societes':societes}
  return render(request,'a-societelist.html',context)

  


def Delete_societe(request,pk):
  deletSociete=Societe.objects.get(id=pk)
  deletSociete.delete()
  societes=Societe.objects.all()
  context={'societes':societes}
  return render(request,'a-societelist.html',context) 

def Activer_societe(request,pk):
            
            societes=Societe.objects.get(id=pk)
            societes.active=True
            societes.save()
            societess=Societe.objects.all()
            for so in societess:
                   if so.id != societes.id:
                      so.active=False
                      so.save()
            context={'societes':societess}
            return render(request,'a-societelist.html',context) 
