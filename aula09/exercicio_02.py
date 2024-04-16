lista = []
for i in range (5):
    v = int(input(f"Digite o valor {i+1}: "))
    lista.append(v)

print(lista)

maximo = max(lista)
print(f"O maior valor é: {maximo}")
print(f"A sua posição é: {lista.index(maximo)}")