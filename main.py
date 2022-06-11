import os
import re

def main():
    if os.path.isdir('LandingPage'):
        if not os.path.isdir('LandingPage/img'):
            os.mkdir('LandingPage/img')
    else:
        os.mkdir('LandingPage')
        os.mkdir('LandingPage/img')


    file = open('form.csv', 'r')         # Salva o arquivo na variavel file
    list = []
    for row in file:
            list.append(row)        # Salva as respostas em rows

    index = 1
    while index < len(list):
        answers = list[index].split(',')
        title = answers[1]
        color = answers[2]
        rows = int(answers[3])
        columns = int(answers[4])
        productName = answers[6].split(';')
        description = answers[7].split(';')

        gerate('<!DOCTYPE html>\n<html>\n<head>\n<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">\n<meta name="charset" content="utf-8"/>\n<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n<style>\n.container-fluid {\npadding-right:0;\npadding-left:0;\nmargin-right:auto;\nmargin-left:auto\n}\n</style>\n', index)
        gerate(f'<title>{title}</title>\n</head>\n<body>\n', index)


        if color == 'Azul':
            gerate(f'<div class="bg-primary">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n', index)
        elif color == 'Cinza':
            gerate(f'<div class="bg-secondary">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n', index)
        elif color == 'Verde':
            gerate(f'<div class="bg-success">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n', index)
        elif color == 'Vermelho':
            gerate(f'<div class="bg-danger">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n', index)
        elif color == 'Amarelo':
            gerate(f'<div class="bg-warning">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n', index)
        elif color == 'Azul claro':
            gerate(f'<div class="bg-info">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n', index)
        elif color == 'Branco':
            gerate(f'<div class="bg-light">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n', index)
        elif color == 'Preto':
            gerate(f'<div class="bg-dark">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n', index)

        color = answers[5]

        if color == 'Azul':
            cardColor = 'bg-primary'
        elif color == 'Cinza':
            cardColor = 'bg-secondary'
        elif color == 'Verde':
            cardColor = 'bg-success'
        elif color == 'Vermelho':
            cardColor = 'bg-danger'
        elif color == 'Amarelo':
            cardColor = 'bg-warning'
        elif color == 'Azul claro':
            cardColor = 'bg-info'
        elif color == 'Branco':
            cardColor = 'bg-light'
        elif color == 'Preto':
            cardColor = 'bg-dark'

        i = 0
        imageName = os.listdir('LandingPage/img')
        while rows > 0:
            col = columns
            gerate('<div class ="container-fluid row text-center">\n', index)
            while col > 0:
                gerate(f'<div class="card col {cardColor}" style="width: 18rem; margin:15px; border:1px solid black;">\n<img src="./img/{imageName[i]}" class="card-img-top" alt="..." width="286" height="240">\n<div class="card-body">\n<h5 class="card-title">{productName[i]}</h5>\n<p class="card-text">{description[i]}</p>\n<a href="#" class="btn btn-primary">Comprar</a>\n</div>\n</div>\n', index)
                i += 1
                col -= 1
            gerate('</div>\n', index)
            rows -= 1
        gerate('</div>\n</body>\n</html>', index)
        index += 1

    print('Sua(s) landing page(s) esta(ão) pronta(s), agora coloque suas imagens dentro da pasta img.')
    print('Não se esqueça de colocar as pastas CSS e JS do bootstrap na mesma pasta da sua landing page.')

def gerate(code, index):
    file = open(f'LandingPage/landingPage{index}.html', 'a')
    file.write(code)

def rename():
    images = os.listdir('LandingPage/img')

    if len(images) > 0:
        i = 0
    for image in images:
        name = images[i].split(" ")[0]                                              # Encontra o nome da imagem
        name = name.split('.')[0]
        last = len(images[i].split("."))                                            # Encontra a ultima palavra da imagem
        extension = images[i].split(".")[last - 1]                                  # Define a ultima palavra como a extensão
        imageName = f'{name}.{extension}'                                           # Define o nome completo da imagem junto com a extensão
        os.rename(f'LandingPage/img/{images[i]}', f'LandingPage/img/{imageName}')   # Troca o nome da imagem
        i += 1

if __name__ == '__main__':
    main()