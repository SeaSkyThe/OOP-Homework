import sys
del sys.path[0]
sys.path.insert(0, '..')

from modelo.Emprestimo import *
from modelo.Livro import *
from modelo.Usuario import *


class Database():
    instancia = None  #variavel estatica
    def __init__(self):
        self.__usuarios = [] #array que guarda objetos do tipo Usuario
        self.__emprestimos = [] #array que guarda objetos do tipo Emprestimo
        self.__livros = [] #array que guarda objetos do tipo Livro


    @staticmethod
    def getInstance():   #nao tem "self" porque o "self" se refere ao objeto, e o metodo estatico será chamado sem a necessidade de um objeto criado
        if(Database.instancia == None):
            Database.instancia = Database()

        return Database.instancia

    def addUsuario(self, usuario): #parametro do tipo Usuario(Aluno ou Professor)
        self.__usuarios.append(usuario)

    def addLivro(self, livro): #parametro do tipo Livro
        self.__livros.append(livro)

    def getNumEmprestimos(self):
        return len(self.__emprestimos)
