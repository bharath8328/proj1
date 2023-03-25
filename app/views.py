from django.shortcuts import redirect,render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.

def index(request):
    var="chirantan"
    return render(request,'index.html',{'name':var})

def persons(request):
    #list=[]
    list=[{'name':'bharath','age':20},{'name':'me','age':21}]
    return render(request,'persons.html',{'persons':list})

def login(request):
    return render(request,'login.html')
def thankyou(request):
    return render(request,'thankyou.html')