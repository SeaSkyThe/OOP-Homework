#Pode ser abstrata??

class Config:
    def __init__(self):
        self.__arquivoLivros = "../archives/livros.pickle" #Verificar se funciona
        self.__arquivoUsuarios = "../archives/usuarios.pickle"
        self.__arquivoEmprestimos = "../archives/emprestimos.pickle"
        self.__diasAluno = 10  #tempo de emprestimo
        self.__diasProfessor = 15


    def getArquivoEmprestimos(self):
        return self.__arquivoEmprestimos


    def setArquivoEmprestimos(self, arquivoEmprestimos):
        self.__arquivoEmprestimos = arquivoEmprestimos


    def getArquivoLivros(self):
        return self.__arquivoLivros


    def setArquivoLivros(self, arquivoLivros):
        self.__arquivoLivros = arquivoLivros


    def getArquivoUsuarios(self):
        return self.__arquivoUsuarios


    def setArquivoUsuarios(self, arquivoUsuarios):
        self.__arquivoUsuarios = arquivoUsuarios


    def getDiasAluno(self):
        return self.__diasAluno


    def setDiasAluno(self, diasAluno):
        self.__diasAluno = diasAluno


    def getDiasProfessor(self):
        return self.__diasProfessor


    def setDiasProfessor(self, diasProfessor):
        self.__diasProfessor = diasProfessor
