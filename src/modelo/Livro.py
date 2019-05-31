class Livro:
    def __init__(self, codLivro, nome, ano):
        self.__codLivro = codLivro
        self.__nome = nome
        self.__ano = ano
        self.__emprestado = False

    def getAno(self):
        return self.__ano

    def setAno(self, ano):
        self.__ano = ano

    def getCodLivro(self):
        return self.__codLivro

    def setCodLivro(self, codLivro):
        self.__codLivro = codLivro

    def estaEmprestado(self):     #retorna True or False
        return self.__emprestado

    def setEmprestado(self, emprestado):   #argumento True or False
        self.__emprestado = emprestado

    def emprestar(self):
        self.__setEmprestado(True)

    def devolver(self):
        self.__setEmprestado(False)

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome
