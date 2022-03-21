print('Escolha o que deseja comprar')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual o seu produto?'))
qtd = int(input('Quantas unidades?'))
if (produto == 1):
    pagar = qtd * 2.3
    print('Você comprou {} macas. Total a pagar: {}'. format(qtd, pagar))
elif (produto == 2):
    pagar = qtd * 3.6
    print('Você comprou {} Laranjas. Total a pagar: {}'.format(qtd, pagar))
elif (produto == 3):
    pagar = qtd * 1.85
    print('Você comprou {} Bananas Total a pagar: {}'.format(qtd, pagar))
elif (nota >= 9.0 and nota <= 10.0):
    print('O aluno {} tirou nota {} e se enquadra no conceito D'.format(nome, nota))
