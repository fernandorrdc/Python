# Listas

# > ante variáveis
n1 = 6,25
n2 = 3,2
n3 = 5,5

#listas

notas = [6,25, 3,2 , 5,5]

#vazia

li = []
li =list()

# acita todos os formatos

lista = [35 , "Fernando" ,  1.77, True, 22, 7]

lista_lista = [10, [ 8 , 2]]

# indexação - acessar

print(lista[0])

#indíces negativos - último
print(lista[-1])

#slice - fatiamentos - pedaços
print(lista[0:3])
print(lista[1:])
print(lista[1:6:2]) #inicia indice 1 vai até 5 de 2 em 2 -range-

#uso do for para percorrer a lista

for i in lista:
    print(i)
print("\n")


#leitura da qtd de elementos len - lenght (comprimento)
print("Qtd itens" ,len(lista))
print("\n")
# for para impressao da lista co range

for i in range(len(lista)):
    print(i, "-",lista[i])
print("\n")
# > Métodos de Lista

#append - insere no final da lista
Listas = [2 , 7 , 13 , 24 ,43]
Lista2 = [1.2 , 0.3]
print("antes do appendice:", Listas)

Listas.append(50)

print("depois do appendice:", Listas)
print("\n")

#insert - indicamos o índice e o valor

Listas.insert(2, "ana") #indice 2 valor ana
print("depois do insert:", Listas)

# extand -juntar 2 listas
Listas.extend(Lista2)
print("Depois do extend:",Listas)

#pop - exclui elementos:
"""
pop()  exclui último índice
pop(1) exclui o indice 1

"""
Listas.pop()
print("retirando último elemento",Listas)
Listas.pop(0)
print("retirando primeiro elemento",Listas)

#remove  - retira o ELEMENTO - não índice -caso tenha mais de um elemento repetido só remove o 1º

Listas.remove("ana")
print("retirando ana da lista",Listas)

#count - contagem de elementos
Listas.append(7)
print("Acrescentando 7 no final:",Listas)

print("Qtd de n. 7 tem na Lista: ",Listas.count(7))
print("indice do elemento 13: ",Listas.index(13))

# sort - Ordenando a lista 

Listas.sort()
print("Ordem Crescente da Lista;",Listas)
Listas.sort(reverse=True)
print("Ordem DeCrescente da Lista;",Listas)

#funções
#sum
print("soma dos elementos da Lista:" , sum(Listas))

#max
print("Maior elemento da Lista:" , max(Listas))

#min
print("menor elemento da Lista:" , min(Listas))
