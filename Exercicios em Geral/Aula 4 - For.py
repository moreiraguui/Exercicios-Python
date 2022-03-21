for x in range (1, 6, 1): #Sempre para um antes, no caso 6 - 1 = 5
    print(x)

#exemplo entre os dois

x = 1
while (x < 6):
    print(x)
    x += 1
    
soma = 0
qtd = 0
for i in range (1,101):
    if (i % 2 ==0):
        soma += 1
        qtd += 1
media = soma / qtd
print('A média dos pares de 1 até 100 é: {}'.format(media))