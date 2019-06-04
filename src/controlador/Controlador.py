import sys
del sys.path[0]
sys.path.insert(0, '..')

from modelo.Biblioteca import Biblioteca


#Rever a questão de instancia do controlador
class Controlador:
    def __init__(self):
        self.__biblio = Biblioteca()

    def getConfiguracoes():
        return self.__biblio.getConfiguracoes

    def addAluno(self, codUsuario, nome, curso, ano):
        self.__biblio.addAluno(codUsuario, nome, curso, ano)

    def addProfessor(self, codUsuario, nome, titulacao):
        self.__biblio.addProfessor(codUsuario, nome, titulacao)

    def addLivro(self, codLivro, nome, ano):
        self.__biblio.addLivro(codLivro, nome, ano)

    def getNumEmprestimos(self):
        self.__biblio.getNumEmprestimos()
