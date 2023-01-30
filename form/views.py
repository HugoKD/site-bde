from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ContactModel

def dejeuner(request):
    if request.method == 'POST':
            nom= request.POST.get('Nom')
            prenom = request.POST.get('Prenom')
            adresse = request.POST.get('Adresse')
            message = request.POST.get('Message')
            vieux = request.POST.get('Vieux')
            couvert = request.POST.get('Couvert')
            horaire = request.POST.get('Horaire')
            NewComamande = ContactModel.objects.create(Nom= nom, Prenom=prenom, Adresse=adresse, Message=message, Vieux=vieux,Couvert=couvert,Horaire=horaire)
            NewComamande.save()
            print(request.POST.get('nom'))


            #form.save()
            return HttpResponseRedirect('/redirection/')

    #else:
        #form = ContactForm()

    return render(request, "form/dejeuner.html")

def redirection(request):
    return render(request, "form/redirection.html")