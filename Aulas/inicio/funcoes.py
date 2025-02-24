# criando função 1

def saudacoes():
    print("seja bom vindo!")

saudacoes()

#uso de parãmetro:
def saudacoes(nome):
    print(f"seja bom vindo!, {nome}")

saudacoes('Miguel')

# mais de um parâmetro

def saudacoes(nome, curso):
    print(f"seja bom vindo!, {nome} \n ao curso de {curso}")

saudacoes("Ricardo" , "python")
saudacoes("alison" , "Java")

#usando defaut
def saudacoes(nome, curso="python"):
    print(f"seja bom vindo!, {nome} \n ao curso de {curso}")

saudacoes("alves"  )

# >> usando retorno

def soma(n1 , n2):
    return n1 + n2 # depois do retur morre abaixo identado nada acontesse.
    

result = soma(7,9)
print(f'o resultado da Soma é :{result}')