valor_hora = float(input("Digite o valor da hora: "))
quantidade_hora = int(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * quantidade_hora

if salario_bruto <= 900:
    ir = 0
    aliquota = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
    aliquota = 5
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.1
    aliquota = 10
else:
    ir = salario_bruto * 0.2
    aliquota = 20

inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11
sindicato = salario_bruto * 0.03
total_descontos = ir + inss
salario_liquido = salario_bruto - total_descontos

print("Salário Bruto: (", valor_hora, "*" , quantidade_hora, "): R$", salario_bruto)
print("(-) IR (", aliquota, "%)               : R$ ", ir)
print("(-) INSS (10%)              : R$ ", inss)
print("FGTS (11%)                  : R$ ", fgts)
print("Total de descontos          : R$ ", total_descontos)
print("Salário Líquido             : R$ ", salario_liquido)