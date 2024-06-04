with open("texto.txt", "r", encoding="utf-") as arquivo:
    for linha in arquivo:
        print(linha.strip())

print("Fim do arquivo")