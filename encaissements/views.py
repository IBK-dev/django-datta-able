from django.core.checks import messages
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Encaissements#, simpleUser

 
# Create your views here.

def encaiss(request):
     if request.user.is_staff:
      encaissem = Encaissements.objects.all()
      context={'encaissem':encaissem}
      return render(request,'b-encaissementslist.html',context)

     else:
       enc=simpleUser.objects.get(user=request.user.id)
       encaissem=enc.encaissem.all()
       context={'encaissem':encaissem}

     return render(request,'b-encaissementslist.html',context)

def encaisscreation(request):
 
    if request.method=='POST':
     if request.POST.get('Numéro_Facture'):
           savecord=Encaissements()
           print("Hollo world")
           savecord.Numéro_Facture = request.POST.get('Numéro_Facture')
           savecord.Date_Facture = request.POST.get('Date_Facture')
           savecord.Client = request.POST.get('Client')
           savecord.Nature = request.POST.get('Nature')
           savecord.Référence = request.POST.get('Référence')
           savecord.Code_TVA = request.POST.get('Code_TVA')
           savecord.Montant_HT = request.POST.get('Montant_HT')
           savecord.Montant_TVA = request.POST.get('Montant_TVA')
           savecord.Montant_TTC = request.POST.get('Montant_TTC')
           
           

           savecord.save()
           messages.success(request,'creation succes...')
           encaissem=Encaissements.objects.all()
           context={'encaissem':encaissem}
           return render(request,'b-encaissementslist.html',context)
    encaissem=Encaissements.objects.all()
    context={'encaissem':encaissem}
    return render(request,'b-encaissementscreat.html',context)