#Programa denominado de Lista de Produtos em ordem crescente.
#Dentro do dicionario o programa ira armazenar o código, o estoque, e o minimo.
#No final do programa ele mostrara as informações que foram colocadas dentro do dicionario, um print mostrando as
#informações do código, estoque e minimo, sendo o código em forma crescente e consequentemente os outros também.

lista = []

#Função

def cadastro_item(item_cadastro: dict): #Função criada para as informações serem inseridas na lista criada a cima
    lista.append(item_cadastro)
    return

#Programa Principal

op = int(input('Você deseja cadastrar um produto? 0 - Não     1 - Sim '))
while (op == 1):
    produto1 = {} #Dicionario

    produto1['codigo'] = int(input('Digite o código do produto: ')) #codigo/estoque/minimo inseridos no dicionario.

    if produto1['codigo'] == 0:
        print('Opção 0 selecionada. Encerrando o cadastro de produtos...') #Função solicitada no enunciado do problema, quando digitado 0 (encerrar o programa)
        break

    produto1['estoque'] = int(input('Digite a quantidade em estoque: ')) #Aqui solicito a qtd em estoque para armazenar no indice estoque para armazenar no dicionario produto1
    produto1['minimo'] = int(input('Digite a quantidade mínima do estoque: '))#Aqui solicito a qtd min e para armazenar no indice min para armazenar no dicionario produto1

    cadastro_item(produto1)
    op = int(input('Você deseja cadastrar  um novo produto? 0 - Não     1 - Sim '))

if len(lista) > 0: #Caso a lista tenha algum valor, a tabela será mostrada.
    print("Código".center(12), end='') #Metodo de string (center). para centralizar a palavra.
    print("Estoque".center(12), end='')
    print("Mínimo".center(12))

    for produto in sorted(lista, key=lambda item: item['codigo']): #utilizada o metodo lambda
        print(str(produto['codigo']).center(12), end='') #Interpretando o código como uma string (srt).
        print(str(produto['estoque']).center(12), end='')#utilizando nomeclatura end para quebra de linha.
        print(str(produto['minimo']).center(12))
else:
    print('Encerrando o Programa...')