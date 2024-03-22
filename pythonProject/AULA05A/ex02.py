nota_1 = float(input("Digite o valor da primeira prova: "))
nota_2 = float(input("Digite o valor da segunda prova: "))

media = (nota_1 + nota_2) / 2

if  (media >=9):
    conceito = "A"
    status = "APROVADO"

elif (media >=7.5):
    conceito = "B"
    status = "APROVADO"

elif (media >=6):
    conceito = "C"
    status = "APROVADO"

elif (media >=4):
    conceito = "D"
    status = "REPROVADO"

elif (media >=0):
    conceito = "E"
    status = "REPROVADO"

print("Você tirou", nota_1, "na primeira prova e", nota_2, "na segunda prova.")
print("Sua média é:", media,)
print("Seu conceito é:", conceito,)
print("Você está:", status,)