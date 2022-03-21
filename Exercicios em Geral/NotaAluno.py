nome = input('Nome do Aluno:')
nota = float(input('Nota Final:'))


if (nota >= 0 and nota <= 2.9):
    print('O aluno {} tirou nota {} e se enquadra no conceito E'.format(nome, nota))
elif (nota >= 3.0 and nota <= 4.9):
    print('O aluno {} tirou nota {} e se enquadra no conceito D'.format(nome, nota))
elif (nota >= 5.0 and nota <= 6.9):
    print('O aluno {} tirou nota {} e se enquadra no conceito C'.format(nome, nota))
elif (nota >= 7.0 and nota <= 8.9):
    print('O aluno {} tirou nota {} e se enquadra no conceito B'.format(nome, nota))
elif (nota >= 9.0 and nota <= 10.0):
    print('O aluno {} tirou nota {} e se enquadra no conceito D'.format(nome, nota))