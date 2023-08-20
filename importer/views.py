from django.shortcuts import render, redirect, get_object_or_404
from .models import Importer
from account.models import Profile, User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

import time
import datetime
import smtplib

def importerInfo(request):
    importers = Importer.objects.all()
    context = {
        'importers': importers
    }
    return render(request, 'importer/index.html', context)


def contactView(request, id=None):
    importer = get_object_or_404(Importer, id=id)
    context ={
        'importer' : importer,
    }
    return render(request, 'importer/contact.html', context)


def infosub1(request, id):
    importer = get_object_or_404(Importer, id=id)
    user_info = Profile.objects.get(user=request.user)
    if request.method =='POST':
        url = request.POST.get('website')
    
    

    context ={
        'importer' : importer,
        'user_info' : user_info,
        'website' : url,
        
    }
    return render(request, 'importer/info2.html', context)

def infosub2(request, id,):
    importer = get_object_or_404(Importer, id=id)
    user_info = Profile.objects.get(user=request.user)
    if request.method =='POST':
        website = request.POST.get('url')
        details = request.POST.get('details')
        size = request.POST.get('size')
        color = request.POST.get('color')
    
    context ={
        'importer' : importer,
        'user_info' : user_info,
        'website' : website,
        'details' : details,
    }
    return render(request, 'importer/preview.html', context)

def sendEmail(request):
    try:
        if request.method == 'POST':
            imp_email = [request.POST.get('email')]
            details = request.POST.get('details')
            product_url = request.POST.get('url')
            message = [details, product_url]
            user_email = request.user
            subject = f"Request for Import Product"
            """ send_mail(subject, details, user_email, imp_email) """
            return render(request, 'importer/emailsuccess.html')

    except BadHeaderError as e:
        return HttpResponse("Invalid header found.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
        
    



