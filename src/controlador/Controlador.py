import sys
del sys.path[0]
sys.path.insert(0, '..')

from modelo.Biblioteca import Biblioteca
from modelo.Professor import *
from modelo.Aluno import *

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
        return self.__biblio.getNumEmprestimos()


    #retornar lista de usuarios
    def getUsuarios(self):
        return self.__biblio.getUsuarios()

    def getAlunos(self):
        alunos = []
        usuarios = self.getUsuarios()
        for usuario in usuarios:
            if isinstance(usuario, Aluno):
                alunos.append(usuario)
        return alunos

    def getProfessores(self):
        professores = []
        usuarios = self.getUsuarios()
        for usuario in usuarios:
            if isinstance(usuario, Professor):
                professores.append(usuario)

        return professores

    def getEmprestimos(self):
        return self.__biblio.getEmprestimos()


    def getNumEmprestimosUsuario(self, usuario):
        emprestimos = self.getEmprestimos()
        numEmprestimos = 0
        for emprestimo in emprestimos:
            if(emprestimo.getCodUsuario() == usuario.getCodUsuario()):
                numEmprestimos += 1

        return numEmprestimos

    #verifica se o usuario tem livros para devolver
    def UsuarioComEmprestimo(self, usuario):
        emprestimos = self.getEmprestimos()
        for emprestimo in emprestimos:
            if(emprestimo.getCodUsuario() == usuario.getCodUsuario()):
                return True
        return False
