class Funcionario:
    def __init__(self, valor_hora, horas_trabalhadas):
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas
        self.salario_bruto = self.calcular_salario_bruto()
        self.desconto_ir = self.calcular_desconto_ir()
        self.desconto_inss = self.calcular_desconto_inss()
        self.fgts = self.calcular_fgts()
        self.total_descontos = self.calcular_total_descontos()
        self.salario_liquido = self.calcular_salario_liquido()

    def calcular_salario_bruto(self):
        return self.valor_hora * self.horas_trabalhadas

    def calcular_desconto_ir(self):
        if self.salario_bruto <= 900:
            return 0
        elif self.salario_bruto <= 1500:
            return self.salario_bruto * 0.05
        elif self.salario_bruto <= 2500:
            return self.salario_bruto * 0.10
        else:
            return self.salario_bruto * 0.20

    def calcular_desconto_inss(self):
        return self.salario_bruto * 0.10

    def calcular_fgts(self):
        return self.salario_bruto * 0.11

    def calcular_total_descontos(self):
        return self.desconto_ir + self.desconto_inss

    def calcular_salario_liquido(self):
        return self.salario_bruto - self.total_descontos

    def imprimir_folha_pagamento(self):
        print(f"Salário Bruto: ({self.valor_hora} * {self.horas_trabalhadas})        : R$ {self.salario_bruto:,.2f}")
        if self.desconto_ir > 0:
            print(f"(-) IR ({int(self.desconto_ir / self.salario_bruto * 100)}%)                     : R$ {self.desconto_ir:,.2f}")
        else:
            print(f"(-) IR (0%)                     : R$ 0,00")
        print(f"(-) INSS (10%)                 : R$ {self.desconto_inss:,.2f}")
        print(f"FGTS (11%)                      : R$ {self.fgts:,.2f}")
        print(f"Total de descontos              : R$ {self.total_descontos:,.2f}")
        print(f"        Salário Líquido                 : R$ {self.salario_liquido:,.2f}")


valor_hora = float(input("Digite o valor da hora: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))
funcionario = Funcionario(valor_hora, horas_trabalhadas)
funcionario.imprimir_folha_pagamento()
