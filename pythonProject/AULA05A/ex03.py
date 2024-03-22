a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if  (a+b<c) or (b+c<a) or (a+c<b):
    print("não é um triangulo")
elif (a==b==c):
    print("é um triangulo equilátero")
elif (a==b) or (b==c) or (a==c):
    print("é um triangulo isósceles")
else:
    print("é um triangulo escaleno")