preco = float(input('Digite o preco do produto:'))
p = float(input('Digite o percentual de desconto (0-100)%:'))

desconto = preco*(p/100)
final = preco-desconto

print('O Preco do produto é {}. Desconto será de {}.'.format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}.'.format(desconto, final))