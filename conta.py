class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # 2 anderlaines para encapsular atributo e fazer com que o programador tenha que utilizar os metodos para
        # alterar ou acrescentar valor neles
        # none = nulo

    def extrato(self):
        print("O saldo do titular {} é de {}".format(self.__titular, self.__saldo))

    def __pode_sacar(self, valor):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou o limite".format(valor))

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def cod_banco():
        return "001"

    @staticmethod  # metodo estatico, ela é da classe e foge da orientacao a objetos, ter cuidado
    # #pra procurar chama a classe dps o nome do metodo no caso cod_bancos
    def cod_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}  # dicionario chave dps atributo
