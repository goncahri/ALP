soma_peso = 0
soma_altura = 0
maior_imc = 0
menor_imc = 100

for i in range(1, 6):
    peso = float(input(f"Entre com o peso (kg) da pessoa {i}: "))
    altura = float(input(f"Entre com a altura (metros) da pessoa {i}: "))
    imc = peso / (altura*altura)
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc
    soma_peso = soma_peso + peso
    soma_altura = soma_altura + altura
peso_medio = soma_peso/5
altura_media = soma_altura/5

print(f"O peso médio das pessoas é {peso_medio:5.2f}kg")
print(f"A altura média das pessoas é {altura_media:5.2f}m")
print(f"O maior IMC é {x:5.2f}")
print(f"O menor IMC é {y:5.2f}")
