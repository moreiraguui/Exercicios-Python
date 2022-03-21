#Este programa foi criado com uma função para que após serem inseridos os dados de nome e sobrenome, ele gere um e-mail
# contendo os mesmos, concatenando juntamente com os dois ultimos digitos do meu RU e com o dominio de e-mail correspondente.

#Função
def email(nome: str, sobrenome: str):
    return 'Sr(a). ' +nome+' '+sobrenome+', seu e-mail é ' +nome[0].lower()+sobrenome.lower()+'22@algoritmos.com.br'

#Programa Principal

nome2 = input('Digite o primeiro nome:')
sobrenome2 = input('Digite o último sobrenome:')
print(email(nome2, sobrenome2))