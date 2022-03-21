#a) Se idade é maior que 60, ecreva: "Você tem direito aos Benefícios"
idade = int(input('Digite a sua idade:'))
if (idade > 60):
    print('Você tem direito aos beneficios')

#b) Se dano é maior do que 10 e escudo é igual a 0, escreva: "Você está morto!"

dano = int(input('Digite o dano:'))
escudo = int(input('Digite o escudo:'))
if (dano > 10 and escudo == 0):
    print('Você está morto!')

#c) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em true, escreva: "Você escapou!"

Coordenada = input('Digite uma Direcao:')
if (Norte == True or Sul == True or Leste == True or Oeste == True):
    print('Você escapou!')