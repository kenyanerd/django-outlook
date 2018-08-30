from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse 
from app.authelper import get_signin_url


#create a home view 

def home(request):
  redirect_uri = request.build_absolute_uri(reverse('app:gettoken'))
  sign_in_url = get_signin_url(redirect_uri)
  return HttpResponse('<a href="' + sign_in_url + '">Click here to sign in and view your mail</a>')



"""def gettoken(request):
  return HttpResponse('gettoken view')
"""
def gettoken(request):
    auth_code = request.GET['code']
    return HttpResponse('Authorization code: {0}'.format(auth_code))