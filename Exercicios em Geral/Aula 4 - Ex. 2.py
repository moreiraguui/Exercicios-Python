#Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias para pagar esse mesmo valor.
#Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de R$ 100, 50, 20, 10, 5 e 1.

valor = int(input('Digite o Valor em R$: '))

while True:
    if (valor >= 100):
        cedulas100 = (valor // 100)
        valor -= (cedulas100 * 100) #valor = (valor - cedulas 100 * 100)
        print('Cedulas de 100: {}'.format(cedulas100))
        if not valor:
            break
    if (valor >= 50):
        cedulas50 = (valor // 50)
        valor -= (cedulas50 * 50) #valor = (valor - cedulas 50 * 50)
        print('Cedulas de 50: {}'.format(cedulas50))
        if not valor:
            break
    if (valor >= 20):
        cedulas20 = (valor // 20)
        valor -= (cedulas20 * 20) #valor = (valor - cedulas 20 * 20)
        print('Cedulas de 20: {}'.format(cedulas20))
        if not valor:
            break
    if (valor >= 10):
        cedulas10 = (valor // 10)
        valor -= (cedulas10 * 10) #valor = (valor - cedulas 10 * 10)
        print('Cedulas de 10: {}'.format(cedulas10))
        if not valor:
            break
    if (valor >= 5):
        cedulas5 = (valor // 5)
        valor -= (cedulas5 * 5) #valor = (valor - cedulas 5 * 5)
        print('Cedulas de 5: {}'.format(cedulas5))
        if not valor:
            break
    if (valor >= 1):
        cedulas1 = (valor // 1)
        valor -= (cedulas1 * 1) #valor = (valor - cedulas 1 * 1)
        print('Cedulas de 1: {}'.format(cedulas1))
        break

print('Encerrando o Serviço...')
