produto = print('O que você gostaria de comprar?')
print('1 - Maca')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual o seu produto?'))
qtd = int(input('Quantas unidades?'))
if (produto == 1):
    pagar = qtd * 2.3
    print('Você comprou {} macas. Total a pagar: {}'. format(qtd, pagar))
else:
    if (produto == 2):
        pagar = qtd * 3.6
        print('Você comprou {} Laranjas. Total a pagar: {}'.format(qtd, pagar))
    else:
        if (produto == 3):
            pagar = qtd * 1.85
            print('Você comprou {} Bananas Total a pagar: {}'.format(qtd, pagar))
        else:
            print('Produto Inexistente')