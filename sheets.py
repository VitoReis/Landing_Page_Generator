from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from auth import authentication

SPREADSHEET_ID = 'YOUR_SHEET_ID'
RANGE_NAME = 'Respostas ao formulário 1!B2:AG'

def sheets():
    creds = authentication()
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

        for row in values:          # Encontra a última resposta da planilha
            count += 1
            if count == len(values):
                for column in row:
                    answers.append(column)
        return answers

    except HttpError as err:
        print(err)