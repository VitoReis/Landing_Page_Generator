import os
from sheets import sheets
from drive import drive
from shutil import copyfile


def answerCatcher():
    answers = sheets()
    if os.path.isdir('LandingPage'):        # Verifica se a pasta onde será armazenado o código já existe
        if not os.path.isdir('LandingPage/img'):
            os.mkdir('LandingPage/img')
    else:                                   # Se a pasta onde será armazenado o código não existe então ela será criada
        os.mkdir('LandingPage')
        os.mkdir('LandingPage/img')
# Site
    productNames = []
    productDescriptions = []
    productPrices = []
    productImages = []

    template = int(answers[1])                  # Salva qual template o usuário escolheu
    siteTitle = answers[2]                      # Salva o titulo do site
    menuColor = answers[3]                      # Salva a cor do menu
    cardColor = answers[4]                      # Salva a cor dos cartões de produtos
    textColor = answers[5]                      # Salva a cor dos textos
    productImages.append(answers[6].split('id=')[1])    # Salva a imagem de fundo do site

# Nome dos produtos
    i = 7
    while i <= 27:
        productNames.append(answers[i])
        i += 4

# Descrição dos produtos
    i = 8
    while i <= 28:
        productDescriptions.append(answers[i])
        i += 4

# Preço dos produtos
    i = 9
    while i <= 29:
        productPrices.append(answers[i])
        i += 4

# Imagens dos produtos
    i = 10
    while i <= 30:
        productImages.append(answers[i].split('id=')[1])
        i += 4

# Informações de contato
    whatsapp = answers[31]
    images = drive(productImages)

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
        textColor = 'blue'
    elif textColor == 'Cinza':
        textColor = 'gray'
    elif textColor == 'Verde':
        textColor = 'green'
    elif textColor == 'Vermelho':
        textColor = 'red'
    elif textColor == 'Amarelo':
        textColor = 'yellow'
    elif textColor == 'Azul claro':
        textColor = 'lightblue'
    elif textColor == 'Branco':
        textColor = 'white'
    elif textColor == 'Preto':
        textColor = 'black'

    # Gerando o site
    generation = generator(template, siteTitle, menuColor, cardColor, textColor, productNames, productPrices, productDescriptions, images, whatsapp)
    if generation:
        print('Sua landing page esta pronta.')
    else:
        print('Houve um erro ao gerar a landing page.')

def generator(template, siteTitle, menuColor, cardColor, textColor, productNames, productPrices, productDescriptions, images, whatsapp):
    copyPath = 'LandingPage/landingPage.html'
    backgroundImage = images[0]
    if template == 1:
        templatePath = 'template1.html'
        copyfile(templatePath, copyPath)
        file = open(f'template1.html', 'r')
    else:
        return False

    fileOutput = open(f'LandingPage/landingPage.html', 'w')

    for line in file:
        newLine = line.replace('$$siteTitle$$', f'{siteTitle}')
        newLine = newLine.replace('$$menuColor$$', f'{menuColor}')
        newLine = newLine.replace('$$cardColor$$', f'{cardColor}')
        newLine = newLine.replace('$$textColor$$', f'{textColor}')
        newLine = newLine.replace('$$backgroundImage$$', f'{backgroundImage}')

        for i in range(0, len(productNames)):
            newLine = newLine.replace(f'$$productName{i+1}$$', f'{productNames[i]}')

        for i in range(0, len(productDescriptions)):
            newLine = newLine.replace(f'$$productDescription{i+1}$$', f'{productDescriptions[i]}')

        for i in range(0, len(productPrices)):
            newLine = newLine.replace(f'$$productPrice{i+1}$$', f'{productPrices[i]}')

        for i in range(1, len(images)):
            newLine = newLine.replace(f'$$productImage{i}$$', f'{images[i]}')

        newLine = newLine.replace('$$whatsapp$$', f'{whatsapp}')
        fileOutput.write(newLine)
    return True