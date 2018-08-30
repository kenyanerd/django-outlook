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
request_id = str(uuid.uuid4())
  instrumentation = {'client-request-id': request_id,
                     'return-client-request-id': 'true'}

  headers.update(instrumentation)

  response = None

  if (method.upper() == 'GET'):
      response = requests.get(url, headers=headers, params=parameters)
  elif (method.upper() == 'DELETE'):
      response = requests.delete(url, headers=headers, params=parameters)
  elif (method.upper() == 'PATCH'):
      headers.update({'Content-Type': 'application/json'})
      response = requests.patch(url, headers=headers,
                                data=json.dumps(payload), params=parameters)
  elif (method.upper() == 'POST'):
      headers.update({'Content-Type': 'application/json'})
      response = requests.post(url, headers=headers,
                               data=json.dumps(payload), params=parameters)

  return response
