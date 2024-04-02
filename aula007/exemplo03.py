qtd = 0

frase = input("Digite uma frase: ")
for letra in frase:
    if (letra=='a') or (letra=='A') or (letra=='ã'):
        qtd = qtd + 1
print(f"O numero de vezes da letra é {qtd}")
