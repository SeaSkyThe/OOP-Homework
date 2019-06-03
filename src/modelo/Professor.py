import sys
del sys.path[0]
sys.path.insert(0, '..')

from modelo.Usuario import *


class Professor(Usuario):
    def __init__(self, codUsuario, nome, diasEmprestimo, titulacao):
        super().__init__(codUsuario, nome, diasEmprestimo)
        self.__titulacao = titulacao
        

    def getTitulacao(self):
        return self.__titulacao

    def setTitulacao(self, titulacao):
        self.__titulacao = titulacao




# #ÁREA DE TESTES
#
# usuario1 = Professor(1234, 'Marcelo', '13', 'Mestre')
#
# print(usuario1.getDiasEmprestimo())
# print(usuario1.getCodUsuario())
# print(usuario1.getNome())
# print(usuario1.getTitulacao())
#
# usuario1.setCodUsuario("143")
# print(usuario1.getCodUsuario())
# usuario1.setTitulacao("Doutor")
# print(usuario1.getTitulacao())
