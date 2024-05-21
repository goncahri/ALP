x = str(input("Digite o valor do seu numero: "))
lista = list(x)

valores = []
for val in x:
    valores.append(int(val))

soma = sum(valores)

multiplicacao = 1
for numero in valores:
    multiplicacao *= numero

print(lista)
print(soma)
print(multiplicacao)


