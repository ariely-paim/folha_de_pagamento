def calcular_salario_liquido(valor_hora, horas_trabalhadas):
    salario_bruto = valor_hora * horas_trabalhadas
    
    if salario_bruto <= 900:
        desconto_ir = 0
    elif salario_bruto <= 1500:
        desconto_ir = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        desconto_ir = salario_bruto * 0.10
    else:
        desconto_ir = salario_bruto * 0.20
    
    desconto_inss = salario_bruto * 0.10
    
    fgts = salario_bruto * 0.11
    
    total_descontos = desconto_ir + desconto_inss
    
    salario_liquido = salario_bruto - total_descontos
    
    return salario_bruto, desconto_ir, desconto_inss, fgts, total_descontos, salario_liquido

def imprimir_folha_pagamento(valor_hora, horas_trabalhadas):
    salario_bruto, desconto_ir, desconto_inss, fgts, total_descontos, salario_liquido = calcular_salario_liquido(valor_hora, horas_trabalhadas)
    
    print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas})        : R$ {salario_bruto:,.2f}")
    if desconto_ir > 0:
        print(f"(-) IR ({int(desconto_ir / salario_bruto * 100)}%)                     : R$ {desconto_ir:,.2f}")
    else:
        print(f"(-) IR (0%)                     : R$ 0,00")
    print(f"(-) INSS (10%)                 : R$ {desconto_inss:,.2f}")
    print(f"FGTS (11%)                      : R$ {fgts:,.2f}")
    print(f"Total de descontos              : R$ {total_descontos:,.2f}")
    print(f"        Salário Líquido                 : R$ {salario_liquido:,.2f}")

valor_hora = float(input("Digite o valor da hora: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

imprimir_folha_pagamento(valor_hora, horas_trabalhadas)