#Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triangulo e classifique como:
#a) Equilátero (três lados iguais)
#b) Isósceles (dois lados iguais)            #Lembre-se: Nenhum dos lados pode ser igual a 0 e um lado não pode ser maior do que a semana dos outros 2 (ex. apost - aula 3)
#c) Escaleno (três lados diferentes)

A = int(input('Digite o 1ª Lado do triangulo:'))
B = int(input('Digite o 2ª Lado do triangulo:'))
C = int(input('Digite o 3ª Lado do triangulo:'))

if ((A > 0) and (B > 0) and (C > 0)):
    if ((A + B > C) and (A + C > B) and (B + C > A)):
    # Se você chegou até aqui, é porque o triângulo é válido!
        if((A != B) and (A != C) and (B != C)):
            print('Triangulo Escaleno!')
        else:
            if ((A == B) and (A == C) and (B == C)):
                print('Triangulo Equilatero!')
            else:
                print('Triangulo Isosceles!')
    else:
        print('Ao menos 1 dos valores indicados nao servem para formar um triangulo')
else:
    ('Ao menos 1 dos valores indicados nao servem para formar um triangulo')