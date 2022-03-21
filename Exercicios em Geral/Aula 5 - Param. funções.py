#Exercicio 1
def borda(s1):
    tam = len(s1)
    # Só imprime caso exista algum caractere
    if tam:
        print('+', '-' * tam, '+')
        print('|',s1,'|')
        print('+', '-' * tam, '+')

#Programa principal

borda('Olá Mundo!')
borda('Eu sou o Guilherme...')