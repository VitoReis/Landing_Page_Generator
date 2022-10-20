from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from auth import authentication
from generator import answerCatcher
from time import sleep

SPREADSHEET_ID = 'YOUR_SHEET_ID'
RANGE_NAME = 'Respostas ao formulário 1!B2:AG'
COUNT = 0

def listener():
    global COUNT
    creds = authentication()

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        while 1:
            result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
            values = result.get('values', [])
            if COUNT != len(values):
                COUNT += len(values)
                answerCatcher()
            sleep(60)

    except HttpError as err:
        print(err)

if __name__ == '__main__':
    listener()
