def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": 123, "titular": "Gustavo", "saldo": 100.0, "limite": 1000.0}
    return conta

def deposita(conta, valor):
    conta["saldo"] = conta["saldo"] + valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}". format(conta["saldo"]))

