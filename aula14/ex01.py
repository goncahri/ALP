x = int(input("Indique a quantidade total de cabeças: "))
y = int(input("Indique a quantidade total de patas: "))

coelhos = int((y - 2*x)/2)
patos = int(x - coelhos)

print("O total de coelhos são: " + str(coelhos))
print("O total de patos são: " + str(patos))