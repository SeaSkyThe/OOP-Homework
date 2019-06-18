import sys               ##Redefinindo PATH para a pasta src, para melhorar os imports
del sys.path[0]
sys.path.insert(0, '..')


from controlador.Controlador import *

from modelo.Config import *
from modelo.Aluno import *
from modelo.Professor import *
from modelo.Livro import *

from dados.Database import *

class Biblioteca:
    def __init__(self):
        self.__configuracoes = Config()
        self.__db = Database.getInstance()

    def getConfiguracoes(self):
        return self.__configuracoes

    def setConfiguracoes(self, configuracoes):
        self.__configuracoes = configuracoes

    def addAluno(self, codUsuario, nome, curso, ano):
        aluno = Aluno(codUsuario, nome, self.__configuracoes.getDiasAluno(), curso, ano)
        self.__db.addUsuario(aluno)

    def addProfessor(self, codUsuario, nome, titulacao):
        professor = Professor(codUsuario, nome, self.__configuracoes.getDiasProfessor(), titulacao)
        self.__db.addUsuario(professor)

    def addLivro(self, codLivro, nome, ano):
        livro = Livro(codLivro, nome, ano)
        self.__db.addLivro(livro)



    def getNumEmprestimos(self):
        return self.__db.getNumEmprestimos()

    def getUsuarios(self):
        return self.__db.getUsuarios()
