import sys
del sys.path[0]
sys.path.insert(0, '..')


from modelo import *


#Rever a questão de instancia do controlador
class Controlador:
    def __init__(self):
        self.__biblio = Biblioteca()

    def getConfiguracoes():
        return self.__biblio.getConfiguracoes

    def addAluno(codUsuario, nome, curso, ano):
        biblio.addAluno(codUsuario, nome, curso, ano)

    def addProfessor(codUsuario, nome, titulacao):
        biblio.addProfessor(codUsuario, nome, titulacao)

    def addLivro(codLivro, nome, ano):
        biblio.addLivro(codLivro, nome, titulacao)
