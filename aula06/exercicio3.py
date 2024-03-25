import math

largura = float(input("Digite a largura do seu aposento: "))
comprimento = float(input("Digite o comprimento do seu aposento: "))

porta = 2.1 * 0.8

area = ((2*(2.80*largura)) + (2*(2.80*comprimento))) - porta

print("A área total de pintura do aposento será de:", area, "m²")
print("Você utilizará", math.ceil(area/3), "litros de tinta (aprox.) para pintar seu aposento!")
print("Você utilizará", math.ceil(area/18), "latas de tinta para pintar seu aposento!")
print("Você utilizará", math.ceil(area/3.7), "galões de tinta para pintar seu aposento!")