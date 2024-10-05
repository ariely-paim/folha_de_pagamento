valor_hora = float(input("Digite o valor da hora: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
desconto_inss = salario_bruto*0.1
desconto_sindicato = salario_bruto*0.03
fgts = salario_bruto*0.11

if salario_bruto > 2500:
    desconto_ir = salario_bruto * 0.20
    pctir = 20
elif salario_bruto > 900 and salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
    pctir = 5
elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
    pctir = 10
else:
    desconto_ir = 0
    pctir = 0

total_descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print(f"Salario bruto: R${salario_bruto:.2f}")
print(f"(-)IR({pctir})%): R${desconto_ir:.2f}")
print(f"(-)INSS(10)%): R${desconto_inss:.2f}")
print(f"(-)Sindicato (3%): R${desconto_sindicato:.2f}")
print(f"FGTS: R${fgts:.2f}")
print(f"Total de desconto: R${total_descontos:.2f}")
print(f"Salario liquido: R${salario_liquido:.2f}")