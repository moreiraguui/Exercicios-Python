nome = input('Qual o seu nome?')
idade = int(input('Qual a sua idade?'))
if nome == 'Guilherme':
    print('Olá Guilherme!')
elif idade < 18:
    print('Você não é o Guilherme e é menor de idade!!!!')
elif idade > 200:
    print('Você não existe!')