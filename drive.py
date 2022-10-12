import io
import os
from auth import authentication
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

def drive(imagesIDs):
    creds = authentication()
    try:
        service = build('drive', 'v3', credentials=creds)
        imagesFiles = []

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