class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido. O depósito deve ser um valor positivo.")

    def saque(self, valor):
        if valor > 0 and self.saldo >= valor:
            if len(self.saques) < 3 and valor <= 500:
                self.saldo -= valor
                self.saques.append(valor)
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Limite diário de saques atingido ou valor máximo por saque excedido.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def extrato(self):
        print("Extrato bancário:")
        if len(self.depositos) == 0 and len(self.saques) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo: R$ {self.saldo:.2f}")

        # Exemplo de uso:
banco = Banco()

banco.deposito(1000)
banco.saque(50)
banco.saque(200)
banco.saque(800)
banco.deposito(200)
banco.extrato()