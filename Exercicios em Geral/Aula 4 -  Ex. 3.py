#Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa. Se a pessoa tiver menos de 3 anos de idade, o ingresso será gratuito
# se tiver entre 3 e 12 anos, o ingresso custará R$ 15 reais, se tiver mais de 12 anos, custária R$ 30.

total = 0
dinheiro = 0

while True:
    idade = input('Qual a sua idade?:')
    if (idade == 'sair'):
        print('Acesso finalizado...')
        break
    idade = int(idade)
    total += 1
    if (idade < 3):
        ingresso = 0
    else:
        if (idade > 12):
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso
    break

media = dinheiro / total
print('Total de pessoas: {}'.format(total))
print('Total arrecadado: R$ {}'.format(dinheiro))
print('Média arrecadada: R$ {}'.format(media))
