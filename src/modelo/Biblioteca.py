from Config import *
from src.dados.database import *
from Aluno import *
from Professor import *
from Livro import *

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
