numero = int(input("Digite o valor do seu número menor que 1000: "))

centenas = int(numero / 100)
dezenas = int((numero - (centenas * 100)) / 10)
unidades = (numero - (centenas * 100) - (dezenas * 10))