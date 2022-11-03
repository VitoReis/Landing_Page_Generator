# static:
siteTitle = False
menuColor = False
cardColor = False
textColor = False
backgroundImage = False
whatsapp = False

# dinamic:
productName = False
productNameCount = 0
productDescription = False
productDescriptionCount = 0
productPrice = False
productPriceCount = 0
productImage = False
productImageCount = 0

def reader():
    global siteTitle, menuColor, cardColor, textColor, backgroundImage, whatsapp, productName, productNameCount, \
        productDescription, productDescriptionCount, productPrice, productPriceCount, productImage, productImageCount


    file = open('template1.html', 'r')

    for line in file:
        if line.__contains__('$$siteTitle$$'):
            siteTitle = True

        if line.__contains__('$$menuColor$$'):
            menuColor = True

        if line.__contains__('$$cardColor$$'):
            cardColor = True

        if line.__contains__('$$textColor$$'):
            textColor = True

        if line.__contains__('$$backgroundImage$$'):
            backgroundImage = True

        if line.__contains__(f'$$productName'):
            productName = True
            productNameCount += 1

        if line.__contains__(f'$$productDescription'):
            productDescription = True
            productDescriptionCount += 1

        if line.__contains__(f'$$productPrice'):
            productPrice = True
            productPriceCount += 1

        if line.__contains__(f'$$productImage'):
            productImage = True
            productImageCount += 1

        if line.__contains__('$$whatsapp$$'):
            whatsapp = True
    print(siteTitle, menuColor, cardColor, textColor, backgroundImage, whatsapp, productName, productNameCount,
          productDescription, productDescriptionCount, productPrice, productPriceCount, productImage, productImageCount)

if __name__ == '__main__':
    reader()