import requests 
import uuid 
import json 

graph_endpoint = 'https://graph.microsoft.com/v1.0{0}'

#Generic API Sending 
def make_api_call(method, url, token, payload = NONE, parameters =NONE):
    #SEND all these headers with all api calls 
    headers = {
        'User-Agent' : 'mail_app/1.0',
        'Authorisation' : 'Bearer {0}'.format(token),
        'Accept' : 'application/json' 
    }
    

  #Use these headers to instrument calls. Makes it easier
  # to correlate requests and responses in case of problems
  # and is a recommended best practice.

  
 

def get_me(access_token):
  get_me_url = graph_endpoint.format('/me')

  # Use OData query parameters to control the results
  #  - Only return the displayName and mail fields
  query_parameters = {'$select': 'displayName,mail'}

  r = make_api_call('GET', get_me_url, access_token, "", parameters = query_parameters)

  if (r.status_code == requests.codes.ok):
    return r.json()
  else:
    return "{0}: {1}".format(r.status_code, r.text)