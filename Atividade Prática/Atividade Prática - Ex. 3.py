#Neste programa, a ideia foi de elaborar uma lista, em que eram inseridos nomes e valores referentes as doações, que a cada 10 reais
# doados a pessoa seria inserida automaticamente em uma lista, que no final seriam embaralhadas e devolveria um ganhador
#utilizando das bibliotecas do python, criando novas funções e também utilizando

import random #importando função

doadores = [] #lista de doadores

#Funções

def cadastro(nome: str, doacao: float): #definindo nome como string e o valor da doação como float
    doadores.extend(((nome + ' ') * int(doacao // 10)).split()) #Função Split necessária para que não seja inserido na lista apenas 1 valor para cada nome.
    return

def sorteio():
    random.shuffle(doadores) #Embaralhando os doadores
    print(f'Lista de doadores embaralhada: {doadores}')
    return random.choice(doadores) #Sorteando um doador aleatoriamente

#Programa Principal

opcao = int(input('Você deseja cadastrar um doador? 0 - Não     1 - Sim '))
print('Para concorrer a um sorteio doe um valor de no mínimo R$ 10,00.')

while opcao == 1: #Caso seja escolhida a opção 1, o programa é iniciado e os dados são solicitados.
    doador = input('Nome do doador: ')
    valor = float(input('Valor que deseja doar: '))

    while len(doador.strip()) == 0 or valor < 10: #Caso selecione a opção 0, o programa será encerrado e se for inserido um valor menor do que R$10 o programa retornará ao inicio.
        #utilizando len e a função strip para que se houver inserção de espaços vazios ou numeros o programa volte com a seguinte mensagem abaixo e o programa retorna ao inicio.
        print('É necessário digitar um nome válido para prosseguir')
        doador = input('Nome do doador: ')
        valor = float(input('Valor que deseja doar: '))

    cadastro(doador, valor) #Chamada da função cadastro

    opcao = int(input('Você deseja cadastrar um novo doador? 0 - Não     1 - Sim '))

if len(doadores) > 0:
    print(f'Lista do sorteio: {doadores}')
    print(f'O vencedor(a) do sorteio foi: {sorteio()}') #Chamada da função sorteio