from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Dealer
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def main(request):
   
    if request.method == 'POST':

     contact=Contact()
     user = request.POST.get('username')
     email = request.POST.get('email')
     subject = request.POST.get('about')


     contact.user=user
     contact.email=email
     contact.subject=subject
     if Contact.objects.filter(user=user).exists():
                messages.info(request, 'Username Taken')
     return render(request, 'main.html')   
     contact.save()
     
     
     return render(request, 'data.html')
     
    
   
def data(request):
    all_dealers = Dealer.objects.all
    return render(request, 'Data.html', {'all':all_dealers})
def contactus(request):
    if request.method == 'POST':
        dealer=Dealer()
        user = request.POST.get('username')
        email = request.POST.get('email')
        ph_number = request.POST.get('contact')
        message = request.POST.get('message')
        
        if Dealer.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/contactus')
        elif  Dealer.objects.filter(user=user).exists():
                messages.info(request, 'Name Taken')   
        elif  Dealer.objects.filter(ph_number=ph_number).exists():
                messages.info(request, 'Number is already registered')               
                return redirect('/contactus')
        dealer.user=user
        dealer.email=email
        dealer.ph_number=ph_number
        dealer.message=message
        dealer.save()
        return HttpResponse('<h1>THANKS FOR CONTACT</h1>') 
        
              
    return render(request, 'contactus.html')
    