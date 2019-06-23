#todo: rever questão das datas

import datetime
from Emprestimo import *


class Item:
    def __init__(self, codEmprestimo, codLivro):
        self.__codEmprestimo = codEmprestimo
        self.__codLivro = codLivro

        #Data de devolucao será setada na devolucao do livro, nao é passada no construtor
        #Será do tipo datetime.date
        self.__dataDevolucao = None


    def getDataDevolucao(self):     #retorna um datetime.date
        return self.__dataDevolucao

    def setDataDevolucao(self, dataDevolucao):
        self.__dataDevolucao = dataDevolucao

    def getCodLivro(self):
        return self.__codLivro
