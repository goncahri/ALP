Valor = float(input("Digite o valor da sua compra: "))

if Valor <= 1000.00:
    desconto = "10%"
    calc = 0.1

elif Valor <= 5000.00:
    desconto = "20%"
    calc = 0.2

else:
    desconto = "30%"
    calc = 0.3

print("O valor do desconto é", desconto,"e o valor total da compra é:", "R$", Valor-(Valor*calc))
