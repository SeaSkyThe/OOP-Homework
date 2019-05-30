#Serialização não foi feita na classe


class Usuario:
    def __init__(self, codUsuario, nome, diasEmprestimo):
        self.__codUsuario = codUsuario
        self.__nome = nome
        self.__diasEmprestimo = diasEmprestimo

    def getDiasEmprestimo(self):
        return int(self.__diasEmprestimo)

    def setDiasEmprestimo(self, diasEmprestimo):
        self.__diasEmprestimo = diasEmprestimo

    def getCodUsuario(self):
        return self.__codUsuario

    def setCodUsuario(self, codUsuario):
        self.__codUsuario = codUsuario

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome



#ÁREA DE TESTES

# usuario1 = Usuario(1234, 'Marcelo', '13')
#
# print(usuario1.getDiasEmprestimo())
# print(usuario1.getCodUsuario())
# print(usuario1.getNome())
#
# usuario1.setCodUsuario("143")
# print(usuario1.getCodUsuario())
