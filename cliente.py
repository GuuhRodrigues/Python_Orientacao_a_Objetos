class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title() #title serve para deixa a primeira letra maiuscula

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome


