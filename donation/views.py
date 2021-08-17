from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import NeedPlasma,DonatePlasma
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponse
import requests
import json
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError
from accounts.models import Profile
from django.views.generic.list import ListView
from django.conf import settings
longitude = -80.191788
latitude = 25.761681

user_location = Point(longitude, latitude, srid=4326)

class findDonors(generic.ListView):
    
    
    model = DonatePlasma
    context_object_name = 'donators'
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    user_locationu = Point(location_data['lon'] ,location_data['lat'],srid=4326)
        
    queryset = DonatePlasma.objects.annotate(distance=Distance('location',
    user_locationu)
    ).order_by('distance')[0:6]
    template_name = 'findDonors.html'
    

def needPlasma(request):
    
    if(request.method=='POST'):
        ip = requests.get('https://api.ipify.org?format=json')
        ip_data = json.loads(ip.text)
        res = requests.get('http://ip-api.com/json/'+ ip_data["ip"])
        location_data_one = res.text
        location_data = json.loads(location_data_one)
        
        name= request.POST.get('name')
        email= request.POST.get('email')
        print(location_data)
        user_locationt = Point(location_data['lon'] ,location_data['lat'],srid=4326)
        mobile_number= request.POST.get('mobileNumber')
        age= request.POST.get('age')
        address= request.POST.get('address')
        
        
        gender= request.POST.get('gender')
        
        doc = request.FILES #returns a dict-like object
        doc_name = doc['filename']
        need_plasma= NeedPlasma.objects.create(user=request.user,name= name,location=user_locationt ,person_email= email,person_mobileNumber=mobile_number,person_age = age, person_address= address, person_gender = gender,file_field=doc_name)


        
    
        

       
        need_plasma.save()
        messages.success(request, 'Your form has been submitted.')
        send_mail(
            'MediCare',
            'Your Plasma Request has been submited! We hope you will get plasma soon',
             settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
             )
        return redirect('findDonors')     
        

        
    return render(request , 'needPlasma.html')



class findNeeders(generic.ListView):
    model = NeedPlasma
    context_object_name = 'needers'
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ ip_data["ip"])
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    user_locationu = Point(location_data['lon'] ,location_data['lat'],srid=4326)
        
    queryset = NeedPlasma.objects.annotate(distance=Distance('location',
    user_locationu)
    ).order_by('distance')[0:20]
    template_name = 'findNeeders.html'
    

def donatePlasma(request):
    if(request.method=='POST'):
        ip = requests.get('https://api.ipify.org?format=json')
        ip_data = json.loads(ip.text)
        res = requests.get('http://ip-api.com/json/'+ ip_data["ip"])
        location_data_one = res.text
        location_data = json.loads(location_data_one)
        
        name= request.POST.get('name')
        email= request.POST.get('email')
        
        user_locationt = Point(location_data['lon'] ,location_data['lat'],srid=4326)
        mobile_number=  request.POST.get('mobileNumber')
        age= request.POST.get('age')
        address= request.POST.get('address')
        date=request.POST.get('codate')
        
        
        doc = request.FILES #returns a dict-like object
        doc_covid = doc.get('last_covid_report')
        doc_igg = doc.get('igg_report')
    
       

        donate_plasma= DonatePlasma.objects.create(name= name,location=user_locationt ,person_email= email,igg_report=doc_igg,person_mobileNumber=mobile_number,
                              person_age = age, person_address= address, 
                             date_last_tested_negative=date,last_covid_report=doc_covid)
                           
        donate_plasma.save()
        messages.success(request, 'Your form has been submitted.')
        send_mail(
           'MediOnline',
            'Your form have been submitted succssfully! \n Thanks for support Neddy People',
           settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            )
        return redirect('findNeeders')     
        
        
    return render(request , 'donatePlasma.html')




class NeedDeleteView(ListView):
    model = NeedPlasma
    def get(self, request, post_id):
        delete_post = self.model.objects.get(id=post_id)
        user2=delete_post.user
        print(delete_post.user)
        delete_post.delete()
        messages.success(request, 'Your post has been deleted successfully.')
        return redirect('/')

class DonateDeleteView(ListView):
    model = DonatePlasma
    def get(self, request, post_id):
        delete_post = self.model.objects.get(id=post_id)
        user2=delete_post.user
        print(delete_post.user)
        delete_post.delete()
        messages.success(request, 'Your post has been deleted successfully.')
        return redirect('/')




