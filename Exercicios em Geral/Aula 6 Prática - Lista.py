#Dada uma lista contendo sas notas de alunos em uma disciplina, escreva uma expressão para:
#a) Encontrar quantos alunos tiraram nota 7
#b) Alterar a ultima nota para 4
#c) Enocntrar a maior nota
#d) Ordenar a lista de notas
#e) A média das notas

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# a)
print(notas.count(7))

# b)
notas[-1] = 4 #da direita pra esquerda -1
print(notas)

# c)



#d)

print(notas.sort())

