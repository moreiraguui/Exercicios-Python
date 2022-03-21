import random

doadores = []

def cadastro(nome: str, doacao: float):
    doadores.extend(((nome + ' ') * int(doacao // 10)).split()) #Função Split necessária para que não seja cadastrada apenas 1 valor.
    return

def sorteio():
    random.shuffle(doadores)
    print(f'Lista de doadores embaralhada: {doadores}')
    return random.choice(doadores)

opcao = int(input('Cadastrar doador? 0 - Não     1 - Sim '))

while opcao == 1:
    doador = input('Nome do doador: ')
    valor = float(input('Valor da doação: '))

    while len(doador.strip()) == 0 or valor < 10:
        print('Insira um valor mínimo de R$ 10 para participar do sorteio')
        doador = input('Nome do doador: ')
        valor = float(input('Valor da doação: '))

    cadastro(doador, valor)

    opcao = int(input('Cadastrar doador? 0 - Não     1 - Sim '))

if len(doadores) > 0:
    print(f'Lista de doadores para sorteio: {doadores}')
    print(f'O vencedor(a) foi: {sorteio()}')