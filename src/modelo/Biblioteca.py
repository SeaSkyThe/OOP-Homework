import sys               ##Redefinindo PATH para a pasta src, para melhorar os imports
del sys.path[0]
sys.path.insert(0, '..')


from controlador import Controlador

from modelo.Config import *
from modelo.Aluno import *
from modelo.Professor import *
from modelo.Livro import *
#verificar import

class Biblioteca:
    def __init__(self):
        self.__configuracoes = Config()
        self.__db = Database.getInstance()

    def getConfiguracoes(self):
        return self.__configuracoes

    def setConfiguracoes(self, configuracoes):
        self.__configuracoes = configuracoes

    def addAluno(self, codUsuario, nome, curso, ano):
        aluno = Aluno(codUsuario, nome, config.getDiasAluno(), curso, ano)
        db.addUsuario(aluno)

    def addProfessor(self, codUsuario, nome, titulacao):
        professor = Professor(codUsuario, nome, config.getDiasProfessor(), titulacao)
        db.addUsuario(professor)

    def addLivro(self, codLivro, nome, ano):
        livro = Livro(codLivro, nome, ano)
        db.addLivro(livro)
