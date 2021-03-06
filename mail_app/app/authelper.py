from urllib.parse import quote, urlencode
import base64
import json 
import time
import requests

#Client Id and Secret key

client_id = 'd60f3082-9c4e-4385-80b4-14edac0ed479'
client_secret = 'sgvAVBV125[[^jmhhLMK59'


# Constant strings for OAuth2 flow
# The OAuth authority
authority = 'https://login.microsoftonline.com'

# The authorize URL that initiates the OAuth2 client credential flow for admin consent
authorize_url = '{0}{1}'.format(authority, '/common/oauth2/v2.0/authorize?{0}')

# The token issuing endpoint
token_url = '{0}{1}'.format(authority, '/common/oauth2/v2.0/token')

# The scopes required by the app
scopes = ['openid',
          'User.Read',
          'Mail.Read']


def get_signin_url(redirect_uri):
  # Build the query parameters for the signin url
  params = {'client_id': client_id,
            'redirect_uri': redirect_uri,
            'response_type': 'code',
            'scope': ' '.join(str(i) for i in scopes)
            }

  signin_url = authorize_url.format(urlencode(params))

  return signin_url

def get_token_from_code(auth_code , redirect_uri):
    #build the post form for the token request
    post_data = {
        'grant_type':'authorization_code',
        'code': auth_code,
        'redirect_uri': redirect_uri,
        'scope':' '.join(str(i) for i in scopes),
        'client_id':client_id,
        'client_secret': client_secret
    }

    r = requests.post(token_url, data = post_data)

    try: 
        return r.json()
    except:
        return 'Error retrieving token : {0} - {1}'.format(r.status_code, r.text)


