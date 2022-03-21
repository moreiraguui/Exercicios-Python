def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial(num):
    """
    Calcule a fatorial
    :param num:
    :return:
    """
    fat = 1
    if num == 0:
        return fat
    for i in range (1, num + 1, 1):
        fat *= i # (fat = fat * i)
    return fat

#Programa Principal
x = valida_int('Digite um valor para calcular a fatorial: ', 0, 9999)
print('{}! = {}'.format(x, fatorial(x)))
help(fatorial)