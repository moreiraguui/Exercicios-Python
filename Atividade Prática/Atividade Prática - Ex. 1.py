#Este programa foi criado para que após serem lidos o nome e a nota final do aluno, seja exibida uma mensagem com o nome
#e sua nota final e com isso em qual conceito o aluno se enquadra, seja o conceito (E, D, C, B ou A).
#Criei uma estrututa de condição dentro de um laço de repetição, com algumas definições pré-definidas, como por exemplo
#ao digitar o numero 1 o programa se inicia, pedindo nome e nota final do aluno, caso seja digitado o numero 0
#o programa exibe automaticamente uma mensagem e é encerrado.
#Ao digitar uma nota invalida (Menor que 0 ou maior que 10) exibe-se uma mensagem e o programa volta ao inicio.

print('RU: 3786322')
while True:
    op = input('Inserir dados? 0 - Não             1 - Sim ')
    if (op == '1'):
        nome1 = input('Nome do Aluno:')
        nota = float(input('Nota Final:'))
    elif (op == '0'):
        print('Você decidiu não inserir dados.!')
        break

    if (nota >= 0 and nota <= 2.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito E'.format(nome1, nota))
    elif (nota >= 3.0 and nota <= 4.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito D'.format(nome1, nota))
    elif (nota >= 5.0 and nota <= 6.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito C'.format(nome1, nota))
    elif (nota >= 7.0 and nota <= 8.9):
        print('O aluno {} tirou nota {} e se enquadra no conceito B'.format(nome1, nota))
    elif (nota >= 9.0 and nota <= 10.0):
        print('O aluno {} tirou nota {} e se enquadra no conceito A'.format(nome1, nota))
    else:
        print('Nota Inválida!')

print('Encerrando programa...')
