from __future__ import print_function
import os
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/drive']

def authentication():
    if os.path.isfile('client_secrets.json'):   # Verifica a existencia e acessa o token de autenticação
        secrets = 'client_secrets.json'
        creds = service_account.Credentials.from_service_account_file(secrets, scopes=SCOPES)
        return creds
    else:                                       # Se o token não existe retorna erro
        print('ERROR: No authentication token available')
        return