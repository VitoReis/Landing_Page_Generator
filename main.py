import os
from sheetsAPI import *
from driveAPI import *
from shutil import copyfile


def main():
    answers = catchAnswers()
    if os.path.isdir('LandingPage'):        # Verifica se a pasta onde será armazenado o código já existe
        if not os.path.isdir('LandingPage/img'):
            os.mkdir('LandingPage/img')
    else:                                   # Se a pasta onde será armazenado o código não existe então ela será criada
        os.mkdir('LandingPage')
        os.mkdir('LandingPage/img')
# Site
    template = int(answers[1])                  # Salva qual template o usuário escolheu
    siteTitle = answers[2]                      # Salva o titulo do site
    menuColor = answers[3]                      # Salva a cor do menu
    cardColor = answers[4]                      # Salva a cor dos cartões de produtos
    textColor = answers[5]                      # Salva a cor dos textos
    # backgroundImage = answers[6].split('id=')[1]    # Salva a imagem de fundo do site
    # imagesIDs.append(backgroundImage)

    productNames = []
    productDescriptions = []
    productPrices = []
    productImages = []

# Nome dos produtos
    i = 6
    while i <= 26:
        productNames.append(answers[i])
        i += 4

# Descrição dos produtos
    i = 7
    while i <= 27:
        productDescriptions.append(answers[i])
        i += 4

# Preço dos produtos
    i = 8
    while i <= 28:
        productPrices.append(answers[i])
        i += 4

# Imagens dos produtos
    i = 9
    while i <= 29:
        productImages.append(answers[i].split('id=')[1])
        i += 4

# Informações de contato
    whatsapp = answers[30]
    images = catchImages(productImages)

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
        template1(siteTitle, menuColor, cardColor, textColor, productNames, productPrices, productDescriptions, images, whatsapp)
    elif template == 2:
        template2(siteTitle, menuColor, cardColor, textColor, productNames, productPrices, productDescriptions, images, whatsapp)

    print('Sua landing page esta pronta.')

def template1(siteTitle, menuColor, cardColor, textColor, productNames, productPrices, productDescriptions, images, whatsapp):
    templatePath = 'template1.html'
    copyPath = 'LandingPage/landingPage.html'
    copyfile(templatePath, copyPath)
    backgroundImage = images[0]

    file = open(f'LandingPage/landingPage.html', 'a+')

    for line in file:
        file.write(line.replace('*//siteTitle*//', f'{siteTitle}'))
        file.write(line.replace('*//menuColor*//', f'{menuColor}'))
        file.write(line.replace('*//cardColor*//', f'{cardColor}'))
        file.write(line.replace('*//textColor*//', f'{textColor}'))
        file.write(line.replace('*//backgroundImage*//', f'{backgroundImage}'))

        for i in range(0, len(productNames)):
            file.write(line.replace(f'*//productName{i}*//', f'{productNames[i]}'))

        for i in range(0, len(productDescriptions)):
            file.write(line.replace(f'*//productDescription{i}*//', f'{productDescriptions[i]}'))

        for i in range(0, len(productPrices)):
            file.write(line.replace(f'*//productPrice{i}*//', f'{productPrices[i]}'))

        for i in range(1, len(images)):
            file.write(line.replace(f'*//productImage{i}*//', f'{images[i]}'))

        file.write(line.replace('*//whatsapp*//', f'{whatsapp}'))

def template2(siteTitle, menuColor, cardColor, textColor, productName, productPrice, productDescription, images):
    templatePath = 'template2.html'
    copyPath = 'LandingPage/landingPage.html'
    copyfile(templatePath, copyPath)
    backgroundImage = images[0]


if __name__ == '__main__':
    main()