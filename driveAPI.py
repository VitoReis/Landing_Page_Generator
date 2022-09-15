from __future__ import print_function

import os.path
import io

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']

def catchImages(imagesIDs):
    creds = None

    if os.path.exists('driveToken.json'):
        creds = Credentials.from_authorized_user_file('driveToken.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('driveToken.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)
        imagesFiles = []

        # Para cada ID na lista: faz o download da imagem e salva o nome da imagem
        i = 1
        for ID in imagesIDs:
            file_id = ID

            request = service.files().get_media(fileId=file_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(F'Download da imagen {i} {int(status.progress() * 100)}%')      # Baixa os bytes da imagem

            file_name = os.path.join('LandingPage/img', f'{i}.jpg')     # Salva os bytes em um arquivo .jpg
            img = open(file_name, 'wb')
            img.write(file.getvalue())
            i += 1

        for files in os.listdir('LandingPage/img'):     # Salva o nome das imagens e envia para o arquivo main
            imagesFiles.append(files)
        return imagesFiles

    except HttpError as error:
        print(f'An error occurred: {error}')