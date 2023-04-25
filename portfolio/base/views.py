from django.shortcuts import render, redirect
from time import sleep
data={
        'text':['home','info','experience','contact'],
    }

def home(request):
    template="index.html"
    return render(request,template,data)

def contact(request):
    template="base/contact.html"
    
    return redirect(template)

def experience(request):
    template="base/experience.html"
 
    return render(request,template,data)

def info(request):
    template="base/info.html"
 
    return render(request,template,data)

