#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação:
#R para residências, I para indústrias e c para comércios

print('Quantidade a pagar de energia elétrica.')
qtd = float(input('Qual foi a quantidade consumida em kWh?'))

print('Qual o seu tipo de instalação?')
print('R - Residência.')
print('I - Indústria')
print('C - Comércio')

tipo = input('Digite aqui:')
if (tipo == 'R'):
    if (qtd <= 500):
        preco = 0.40
    else:
        preco = 0.65
elif (tipo == 'I'):
    if (qtd <= 1000):
        preco = 0.55
    else:
        preco = 0.60
elif (tipo == 'C'):
    if (qtd <= 5000):
        preco = 0.55
    else:
        preco = 0.60
print('O valor total a pagar é de: R$ {}'.format(qtd * preco))

print('Fim do cálculo...')


