from django.core.checks import messages
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Deductions#, simpleUser

 
# Create your views here.

def deduct(request):
     if request.user.is_staff:
      deduction = Deductions.objects.all()
      context={'deduction':deduction}
      return render(request,'c-deductionslist.html',context)

     else:
       ded=simpleUser.objects.get(user=request.user.id)
       deduction=ded.deduction.all()
       context={'deduction':deduction}

     return render(request,'c-deductionslist.html',context)

def deducreation(request):
 
    if request.method=='POST':
     if request.POST.get('Numéro_Facture'):
           savecord=Deductions()
           savecord.Numéro_Facture = request.POST.get('Numéro_Facture')
           savecord.Date_Facture = request.POST.get('Date_Facture')
           savecord.Fournisseur = request.POST.get('Fournisseur')
           savecord.Nature = request.POST.get('Nature')
           savecord.Référence = request.POST.get('Référence')
           savecord.Code_TVA = request.POST.get('Code_TVA')
           savecord.Montant_HT = request.POST.get('Montant_HT')
           savecord.Montant_TVA = request.POST.get('Montant_TVA')
           savecord.Montant_TTC = request.POST.get('Montant_TTC')
           savecord.Date_paiement = request.POST.get('Date_paiement')
           savecord.Mode_paiement = request.POST.get('Mode_paiement')
           savecord.Prorata = request.POST.get('Prorata')
           savecord.TVA_déductible = request.POST.get('TVA_déductible')
           savecord.Non_resident = request.POST.get('Non_resident')
           
           

           savecord.save()
           messages.success(request,'creation succes...')
           deduction=Deductions.objects.all()
           context={'deduction':deduction}
           return render(request,'c-deductionslist.html',context)
    deduction=Deductions.objects.all()
    context={'deduction':deduction}
    return render(request,'c-deductionscreat.html',context)