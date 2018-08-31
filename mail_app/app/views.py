from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse 
from app.authelper import get_signin_url
from app.outlookservice import get_me


#updated home view to  
def home(request):
  redirect_uri = request.build_absolute_uri(reverse('app:gettoken'))
  sign_in_url = get_signin_url(redirect_uri)
  return HttpResponse('<a href="' + sign_in_url + '">Click here to sign in and view your mail</a>')
  
#original home view 
'''def old_home(request):
  sign_in_url = '#'
  context = {'sign_in_url': sign_in_url}
  return render(request, 'app/home.html', context)
  '''

"""def gettoken1(request):
  return HttpResponse('gettoken view')
"""
"""
def gettoken2(request):
    auth_code = request.GET['code']
    redirect_uri = request.build['']
    return HttpResponse('Authorization code: {0}'.format(auth_code))
"""
# Add import statement to include new function


def gettoken(request):
  auth_code = request.GET['code']
  redirect_uri = request.build_absolute_uri(reverse('app:gettoken'))
  token = get_token_from_code(auth_code, redirect_uri)
  access_token = token['access_token']
  user = get_me(access_token)

  # Save the token in the session
  request.session['access_token'] = access_token
  return HttpResponse('User: {0}, Access token: {1}'.format(user['displayName'], access_token))


