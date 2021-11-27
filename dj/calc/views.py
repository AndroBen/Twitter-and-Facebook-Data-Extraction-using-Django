from django.shortcuts import render
from django.http import HttpResponse
import facebook
import json
# Create your views here.
def home(request):
    return HttpResponse("Hello")
def htm(request):
    return render(request,'home.html',{'name':'Andro'})
def fb(request):
    idd=request.GET['id']

    token=''
    graph=facebook.GraphAPI(token)
    profile=graph.get_object(idd,fields='id,name,first_name,last_name,link,birthday,gender')
    return render(request,'table.html',{'id':profile["id"],'name':profile["name"],'fname':profile["first_name"],'lname':profile["last_name"],'bday':profile["birthday"],'gender':profile["gender"]})
   

