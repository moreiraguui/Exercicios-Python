# Exercicio 1
def valida_string(pergunte, min, max):
    s1 = input(pergunte)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunte)
        tam = len(s1)
        break
    return s1


#Programa princiapl
x = valida_string('Digite uma string: ', 10, 30)
print('Você digitou a string: {}. \n Dado válido. Encerrando o programa...'.format(x))