from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Caso modifique esse escopo, delete o arquivo token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# ID e alcance da planilha.
SPREADSHEET_ID = 'SHEET ID'
RANGE_NAME = 'Respostas ao formulário 1!B2:K3'


def catchAnswers():
    creds = None
    # O arquivo token.json guarda o acesso do usuário e o token de atualização, e cria
    # automaticamente quando o fluxo de autorização ocorre pela primeira vez.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Se não há credenciais (validas) disponiveis, deixa o usuário fazer log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Salva as credenciais para proxima execução
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        answers = []
        count = 0

        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:              # Se a planilha estiver vazia o programa para
            print('No data found.')
            return

        for row in values:          # Encontra a última resposta da planilha (ultima linha)
            count += 1
            if count == len(values):
                for column in row:
                    answers.append(column)
        return answers

    except HttpError as err:
        print(err)