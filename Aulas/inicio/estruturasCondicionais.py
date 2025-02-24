#ESTRUTURAS CONDICIONAIS

idade = int(input("digite sua idade:"))

if idade >=18 :
    print("ALUNO : Maior de Idade")
else:
    print("ALUNO: menor de Idade")


n1 = float(input("nota AV1:"))
n2 = float(input("nota AV2:"))
media = (n1 + n2)/2

if n1 >10 or n2 > 10:
    print("av1 ou av2 invalia" , n1 , n2)

elif media >=7:
    print("aprovado \n média :" , media)
elif  media >= 5:
    print("recuperação \n média :", media)
 
else:
    print("REPROVADO \n média :" , media) 