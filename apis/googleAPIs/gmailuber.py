import json
import keys

from apiclient import discovery
from oauth2client import client
#import client_secret

secrets_file = "client_secrets.json"

def acquire_oauth2_credentials(secrets_file):
    """Flows through OAuth 2.0 authorization process for credentials."""
    flow = client.flow_from_clientsecrets(
        secrets_file,
        scope='https://www.googleapis.com/auth/gmail.readonly',
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')

    auth_uri = flow.step1_get_authorize_url()
    webbrowser.open(auth_uri)

    auth_code = raw_input('Enter the authentication code: ')

    credentials = flow.step2_exchange(auth_code)
    print(credentials)
    return credentials

acquire_oauth2_credentials(secrets_file)
'''
CLIENTSECRETS_LOCATION = .client_secret
#REDIRECT_URI =
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
]

def exchange_code(authorization_code):
    flow = flow_from_clientsecrets(CLIENTSECRETS_LOCATION, ' '.join(SCOPES))


def store_credentials(user_id, credentials):
    raise NotImplementedError()
'''
