#uso da função range

# o a 5
for i in range(6):
    print(i)
print("\n")

# 1 ao 5
for i in range(1,6):
    print(i)  
print("\n")

# com 3 parâmetrod
# 1 ao 5
for i in range(1, 6 ,2):
    print(i)  
print("\n")

# automatizando 3 notas
soma = 0

for i in range (1,4):
    nota = float(input(f"lançamento da AV{i}:"))
    soma = soma + nota
print("Média :",soma / 3)