import os
from sheetsAPI import *
from driveAPI import *


def main():
    answers = catchAnswers()
    if os.path.isdir('LandingPage'):        # Verifica se a pasta onde será armazenado o código já existe
        if not os.path.isdir('LandingPage/img'):
            os.mkdir('LandingPage/img')
    else:                                   # Se a pasta onde será armazenado o código não existe então ela será criada
        os.mkdir('LandingPage')
        os.mkdir('LandingPage/img')

    template = int(answers[0])                  # Salva qual template o usuário escolheu
    siteTitle = answers[1]                      # Salva o titulo do site
    menuColor = answers[2]                      # Salva a cor do menu
    cardColor = answers[3]                      # Salva a cor dos cartões de produtos
    textColor = answers[4]                      # Salva a cor dos textos
    productName = answers[5].split('&')         # Salva o nome de cada produto
    productPrice = answers[6].split('&')        # Salva o preço de cada produto
    productDescription = answers[7].split('&')  # Salva a descrição de cada produto
    whatsapp = answers[8]                       # Salva o número do whatsapp da loja
    imagesLinks = answers[9].split(',')         # Salva o link das imagens do site
    imagesIDs = []
    for image in imagesLinks:                   # Separa os IDs de cada imagem dos links
        imagesIDs.append(image.split('id=')[1])

    images = catchImages(imagesIDs)

    # Ajuste de cores de acordo com a resposta
    if menuColor == 'Azul':
        menuColor = 'bg-primary'
    elif menuColor == 'Cinza':
        menuColor = 'bg-secondary'
    elif menuColor == 'Verde':
        menuColor = 'bg-success'
    elif menuColor == 'Vermelho':
        menuColor = 'bg-danger'
    elif menuColor == 'Amarelo':
        menuColor = 'bg-warning'
    elif menuColor == 'Azul claro':
        menuColor = 'bg-info'
    elif menuColor == 'Branco':
        menuColor = 'bg-light'
    elif menuColor == 'Preto':
        menuColor = 'bg-dark'

    if cardColor == 'Azul':
        cardColor = 'bg-primary'
    elif cardColor == 'Cinza':
        cardColor = 'bg-secondary'
    elif cardColor == 'Verde':
        cardColor = 'bg-success'
    elif cardColor == 'Vermelho':
        cardColor = 'bg-danger'
    elif cardColor == 'Amarelo':
        cardColor = 'bg-warning'
    elif cardColor == 'Azul claro':
        cardColor = 'bg-info'
    elif cardColor == 'Branco':
        cardColor = 'bg-light'
    elif cardColor == 'Preto':
        cardColor = 'bg-dark'

    if textColor == 'Azul':
        cardColor = 'blue'
    elif textColor == 'Cinza':
        cardColor = 'gray'
    elif textColor == 'Verde':
        cardColor = 'green'
    elif textColor == 'Vermelho':
        cardColor = 'red'
    elif textColor == 'Amarelo':
        cardColor = 'yellow'
    elif textColor == 'Azul claro':
        cardColor = 'lightblue'
    elif textColor == 'Branco':
        cardColor = 'white'
    elif textColor == 'Preto':
        cardColor = 'black'

    if template == 1:
        template1(siteTitle, menuColor, cardColor, textColor, productName, productPrice, productDescription, whatsapp, images)
    elif template == 2:
        template2(siteTitle, menuColor, cardColor, textColor, productName, productPrice, productDescription, whatsapp, images)

    print('Sua landing page esta pronta.')

def generate(code):
    file = open(f'LandingPage/landingPage.html', 'a')
    file.write(code)

def template1(siteTitle, menuColor, cardColor, textColor, productName, productPrice, productDescription, whatsapp, images):
    i = 0
    imageName = []
    # Separa a imagem de fundo das outras imagens
    while i < len(images):
        if images[i].startswith('0'):
            backgroundImage = images[i]
        else:
            imageName.append(images[i])
        i += 1

    generate('<!DOCTYPE html>\n<html>\n<head>\n<meta name="charset" content="utf-8"/>\n<meta name="viewport" '
             'content="width=device-width, initial-scale=1.0"/>\n<link rel="stylesheet" '
             'href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" '
             'integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">\n'
             '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">\n'
             '<!--Espaçamento do container, centralização das linhas e definição da imagem de fundo-->\n<style>\n'
             '.container-fluid {\npadding-right:0;\npadding-left:0;\nmargin-right:auto;\nmargin-left:auto\n}\n'
             '.row{\ntext-align: center;\nmargin: auto;\n}\n.bg-image{\n')


    generate(f'background-image: url(./img/{backgroundImage});''\nbackground-repeat: no-repeat;\nbackground-size: cover;\n}\n'
             '</style>\n')

    generate(f'<title>{siteTitle}</title>\n</head>\n<body class="bg-image">\n')

    generate(f'<div class="border border-dark {menuColor}" style="width: 50rem; margin: auto; margin-top: 1rem;'
             f' margin-bottom: 1rem;">\n')

    generate(f'<div class="container row border border-dark">\n<h1 class="col text-center" style="color: {textColor};">'
             f'{siteTitle}</h1>\n</div>\n<br/>\n')

    i = 0
    for product in productName:
        generate(f'<div class="container text-center">\n<ul class="list-unstyled">\n<li class="media border'
            f' border-dark {cardColor}" style="margin: auto;">\n<img class="mr-3" src="./img/{imageName[i]}"'
            f' alt="Generic placeholder image" style="width: 18rem; height: 13rem; margin: 1rem; border:1px solid black;">\n'
            f'<div class="media-body my-4">\n<h5 class="mt-0 mb-1" style="color: {textColor};">{productName[i]}</h5>\n'
            f'<p style="margin-top: 2rem;  color: {textColor};">{productDescription[i]}</p>\n<h5 style="margin-top: 2rem;'
            f' color: {textColor};">R${productPrice[i]}</h5>\n</div>\n</li>\n</ul>\n</div>\n')
        i += 1

    generate(f'<div class="row text-center">\n<div class="col text-center border border-dark">\n<h4 '
        f'style="color: {textColor};">Contato:</h4>\n<div>\n<a href="https://wa.me/55{whatsapp}" target="_blank">\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-whatsapp" '
        f'viewBox="0 0 16 16" style="color: #118011; margin-bottom: 1rem;">\n<path d="M13.601 2.326A7.854 7.854 0 0 0 '
        f'7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 '
        f'3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.'
        f'356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.'
        f'584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.'
        f'934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.'
        f'148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.'
        f'088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.'
        f'389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .'
        f'977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.'
        f'058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"/>\n</svg>\n</a>\n</div>\n'
        f'</div>\n</div>\n</div>\n</body>\n</html>')

def template2(siteTitle, menuColor, cardColor, textColor, productName, productPrice, productDescription, images):
    print('Template 2')

if __name__ == '__main__':
    main()