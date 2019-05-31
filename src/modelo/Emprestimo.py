import sys
del sys.path[0]
sys.path.insert(0, '..')

from modelo.Usuario import *
from modelo.Aluno import *
from modelo.Professor import *

import datetime
#todo: rever questao de datas
class Emprestimo:
    #Contrutor pede o codigo de emprestimo e um usuario(obj do tipo Usuario)
    def __init__(self, codEmprestimo, usuario):
        self.__codEmprestimo = codEmprestimo
        self.__codUsuario = usuario.getCodUsuario()
        self.__itens = [] #Lista de livros
        self.__dataEmprestimo = datetime.date.today() #Pegando a data atual

        #tratar data de devoulucao
        if(isinstance(usuario, Aluno)):
            self.__dataDevolucao = datetime.date.fromordinal(self.__dataEmprestimo.toordinal()+10) #Data de devolução é 10 dias apos o emprestimo
        else:
            self.__dataDevolucao = datetime.date.fromordinal(self.__dataEmprestimo.toordinal()+15) #Data de devolução é 15 dias apos o emprestimo
        #Falta uma variavel, tirar duvida


    def getCodEmprestimo(self):
        return self.__codEmprestimo

    def setCodEmprestimo(self, codEmprestimo):
        self.__codEmprestimo = codEmprestimo

    def getCodUsuario(self):
        return self.__codUsuario


    def setCodUsuario(self, codUsuario):
        self.__codUsuario = codUsuario


    def getDataDevolucao(self):
        return self.__dataDevolucao


    def setDataDevolucao(self, dataDevolucao):
        self.__dataDevolucao = dataDevolucao


    def getDataEmprestimo(self):
        return self.__dataEmprestimo


    def setDataEmprestimo(self, dataEmprestimo):
        self.__dataEmprestimo = dataEmprestimo

    def getItens(self):
        return self.__itens

    def setItens(self, itens): #argumento é uma lista de objetos do tipo Item
        self.__itens = itens
