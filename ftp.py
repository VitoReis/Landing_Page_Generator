from ftplib import FTP_TLS
from ftplib import all_errors
from os import listdir

HOSTNAME = 'YOUR_HOST_NAME'
USERNAME = 'YOUR_USER_NAME'
PASSWORD = 'YOUR_PASSWORD'

def connect():
    ftps = FTP_TLS()
    ftps.set_pasv(True)
    ftps.connect(HOSTNAME)
    ftps.login(USERNAME, PASSWORD)
    ftps.prot_p()
    try:
        ftps.cwd('/landingPage')
        landingPage = open('LandingPage/landingPage.html', 'rb')
        ftps.storbinary('STOR landingPage.html', landingPage)
        landingPage.close()
        for image in listdir('LandingPage/img'):
            ftps.cwd('/landingPage/img')
            img = open(f'LandingPage/img/{image}', 'rb')
            ftps.storbinary(f'STOR {image}', img)
            landingPage.close()
            img.close()
    except all_errors as ex:
        print(ex)
    finally:
        ftps.quit()

if __name__ == '__main__':
    connect()