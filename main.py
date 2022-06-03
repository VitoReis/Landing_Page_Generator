import os
import patoolib

def main():
    os.mkdir('LandingPage/img')
    patoolib.extract_archive("bootstrap.rar", outdir="LandingPage")
    gerate('<!DOCTYPE html>\n<html>\n<head>\n<script src="js/jquery-3.6.0.min.js" type="text/javascript"></script> \n<link href="css/bootstrap.min.css" rel="stylesheet" type="text/css"/>\n<script src="js/bootstrap.min.js" type="text/javascript"></script>\n<meta name="charset" content="utf-8"/>\n<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n<style>\n.container-fluid {\npadding-right:0;\npadding-left:0;\nmargin-right:auto;\nmargin-left:auto\n}\n</style>\n')
    title = input('Insira o titulo da sua pagina: ')
    gerate(f'<title>{title}</title>\n</head>\n<body>\n')
    color = int(input('Qual destas cores você gostaria para o seu site?\n1 - Azul\n2 - Cinza\n3 - Verde\n4 - Vermelho\n'
                                                            '5 - Amarelo\n6 - Azul claro\n7 - Cinza claro\n8 - Preto\n'))
    if color == 1:
        gerate(f'<div class="bg-primary">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n')
    elif color == 2:
        gerate(f'<div class="bg-secondary">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n')
    elif color == 3:
        gerate(f'<div class="bg-success">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n')
    elif color == 4:
        gerate(f'<div class="bg-danger">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n')
    elif color == 5:
        gerate(f'<div class="bg-warning">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n')
    elif color == 6:
        gerate(f'<div class="bg-info">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n')
    elif color == 7:
        gerate(f'<div class="bg-light">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n')
    elif color == 8:
        gerate(f'<div class="bg-dark">\n<div class ="container-fluid row">\n<h1 class ="col text-center">{title}</h1>\n</div>\n')


    lines = int(input('Seus site sera dividido em quantas linhas? '))
    columns = int(input('Quantas colunas com cartoes seu site tera? '))
    color = int(input('Qual destas cores você gostaria para os seus cartões?\n1 - Azul\n2 - Cinza\n3 - Verde\n4 - Vermelho\n'
                                                                        '5 - Amarelo\n6 - Azul claro\n7 - Cinza claro\n8 - Preto\n'))
    if color == 1:
        cardColor = 'bg-primary'
    elif color == 2:
        cardColor = 'bg-secondary'
    elif color == 3:
        cardColor = 'bg-success'
    elif color == 4:
        cardColor = 'bg-danger'
    elif color == 5:
        cardColor = 'bg-warning'
    elif color == 6:
        cardColor = 'bg-info'
    elif color == 7:
        cardColor = 'bg-light'
    elif color == 8:
        cardColor = 'bg-dark'


    while lines > 0:
        gerate('<div class ="container-fluid row text-center">\n')
        while columns > 0:
            productName = input('Insira o nome do seu produto: ')
            description = input('Insira uma descrição para o seu produto: ')
            imageName = input('Digite o nome da imagem do seu produto (ex: hamburguer.jpg): ')
            gerate(f'<div class="card col {cardColor}" style="width: 18rem; margin:15px; border:1px solid black;">\n<img src="./img/{imageName}" class="card-img-top" alt="..." width="286" height="240">\n<div class="card-body">\n<h5 class="card-title">{productName}</h5>\n<p class="card-text">{description}</p>\n<a href="#" class="btn btn-primary">Comprar</a>\n</div>\n</div>\n')
            columns -= 1
        gerate('</div>\n')
        lines -= 1
    gerate('</div>\n</body>\n</html>')


def gerate(code):
    file = open('LandingPage/landingPage.html','a')
    file.write(code)

if __name__ == '__main__':
    main()