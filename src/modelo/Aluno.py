import sys
del sys.path[0]
sys.path.insert(0, '..')

from modelo.Usuario import *

class Aluno(Usuario):
    def __init__(self, codUsuario, nome, diasEmprestimo, curso, ano):
        super().__init__(codUsuario, nome, diasEmprestimo)
        self.__curso = curso
        self.__ano = ano

    def setCurso(self, curso):
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def setAno(self, ano):
        self.__ano = ano

    def getAno(self):
        return self.__ano
