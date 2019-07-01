import sys
del sys.path[0]
sys.path.insert(0, '..')

import pickle
from modelo.Biblioteca import Biblioteca
from modelo.Professor import *
from modelo.Aluno import *
from modelo.Livro import *
from modelo.Emprestimo import *
from modelo.Item import *

#Rever a questão de instancia do controlador
class Controlador:
    def __init__(self):
        self.__biblio = Biblioteca()

    def getConfiguracoes():
        return self.__biblio.getConfiguracoes()

    def addAluno(self, codUsuario, nome, curso, ano):
        self.__biblio.addAluno(codUsuario, nome, curso, ano)

    def addProfessor(self, codUsuario, nome, titulacao):
        self.__biblio.addProfessor(codUsuario, nome, titulacao)

    def addLivro(self, codLivro, nome, ano):
        self.__biblio.addLivro(codLivro, nome, ano)

    def addEmprestimo(self, codEmprestimo, usuario):
        self.__biblio.addEmprestimo(codEmprestimo, usuario)

    def getNumEmprestimos(self):
        return self.__biblio.getNumEmprestimos()

    def criarListaItens(self, codEmprestimo, livros): #Recebe uma lista de livros e transforma numa lista de itens
        itens = []
        for livro in livros:
            livro.emprestar()
            codLivro = livro.getCodLivro()
            item = Item(codEmprestimo, codLivro)
            itens.append(item)
        return itens

    def addItensEmprestimo(self, codEmprestimo, livros): #recebe uma lista de livros, transforma em lista de itens e adiciona
        emprestimo = self.getEmprestimoCodigo(codEmprestimo)
        codUsuario = emprestimo.getCodUsuario()
        usuario = self.getUsuarioCodigo(codUsuario)
        usuario.addItensHistorico(livros)
        emprestimo.setItens(self.criarListaItens(codEmprestimo, livros))

    #Retornar LISTAS
    def getUsuarios(self):
        return self.__biblio.getUsuarios()

    def getUsuarioNome(self, nome):
        usuarios = self.getUsuarios()
        for usuario in usuarios:
            if(str.lower(nome) == str.lower(usuario.getNome())):
                return usuario
        return None

    def getUsuarioCodigo(self, codigo):
        usuarios = self.getUsuarios()
        for usuario in usuarios:
            if(int(codigo) == int(usuario.getCodUsuario())):
                return usuario
        return None

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

    def getLivros(self):
        return self.__biblio.getLivros()

    #Nao foi possivel utilizar polimorfismo pois é necessaria a conversão de tipos
    def getLivroNome(self, titulo):
        livros = self.getLivros()
        for livro in livros:
            if(str.lower(titulo) == str.lower(livro.getNome())):
                return livro
        return None

    def getLivroCodigo(self, codigo):
        livros = self.getLivros()
        for livro in livros:
            if(int(codigo) == int(livro.getCodLivro())):
                return livro
        return None

    def getCodLivro(self, livro):
        return livro.getCodLivro()

    def getLivrosEmprestadosUsuario(self, codigo):
        emprestimos = self.getEmprestimos()
        emprestimosUsuario = []
        for emprestimo in emprestimos:
            if(int(emprestimo.getCodUsuario()) == int(codigo)):
                emprestimosUsuario.append(emprestimo)

        livrosUsuario = []
        for each in emprestimosUsuario:
            itens = each.getItens()
            for item in itens:
                codLivro = item.getCodLivro()
                livro = self.getLivroCodigo(codLivro)
                livrosUsuario.append(livro)

        return livrosUsuario

    def getEmprestimos(self):
        return self.__biblio.getEmprestimos()

    def getEmprestimoCodigo(self, codEmprestimo):
        emprestimos = self.getEmprestimos()
        for emprestimo in emprestimos:
            if(str.lower(codEmprestimo) == str.lower(emprestimo.getCodEmprestimo())):
                return emprestimo
        return None

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

    def UsuarioComAtraso(self, usuario):
        if(self.UsuarioComEmprestimo(usuario) == False):
            return False
        else:
            emprestimos = self.getEmprestimos()
            codigoUsuario = usuario.getCodUsuario()
            for emprestimo in emprestimos:
                codigoUsuarioEmprestimo = emprestimo.getCodUsuario()
                if(codigoUsuario == codigoUsuarioEmprestimo):
                    itens = emprestimo.getItens()
                    for item in itens:
                        if(emprestimo.getDataDevolucao() < datetime.date.today()):
                            return True
        return False

    def UsuarioTemHistorico(self, usuario):
        if(len(usuario.getHistorico()) > 0):
            return True
        return False

    def livroEstaEmprestado(self, livro):
        if(livro.estaEmprestado() == True):
            return True
        return False

    def livroEstaAtrasado(self, livro):
        if(self.livroEstaEmprestado(livro) == False):
            return False
        else:
            emprestimos = self.getEmprestimos()
            codigoLivro = livro.getCodLivro()
            for emprestimo in emprestimos:
                itens = emprestimo.getItens()
                for item in itens:
                    codigoLivroEmprestimo = item.getCodLivro()
                    if(codigoLivro == codigoLivroEmprestimo):
                        if(emprestimo.getDataDevolucao() < datetime.date.today()):
                            return True
        return False

    def getNumAtrasos(self):
        num = 0
        livros = self.getLivros()
        for livro in livros:
            if(self.livroEstaAtrasado(livro) == True):
                num += 1

        return num


    def saveAll(self):
        dump = self.__biblio.dumpDatabase()
        config = self.__biblio.getConfiguracoes()
        print(config)
        pickle_out = open(config.getArquivoUsuarios(), "wb")
        pickle.dump(dump['usuarios'], pickle_out)
        pickle_out.close()
        pickle_out = open(config.getArquivoEmprestimos(), "wb")
        pickle.dump(dump['emprestimos'], pickle_out)
        pickle_out.close()
        pickle_out = open(config.getArquivoLivros(), "wb")
        pickle.dump(dump['livros'], pickle_out)
        pickle_out.close()


    def loadData(self):
        config = self.__biblio.getConfiguracoes()
        print(config)
        pickle_in = open(config.getArquivoUsuarios(), "rb")
        usuarios = pickle.load(pickle_in)
        pickle_in.close()
        pickle_in = open(config.getArquivoEmprestimos(), "rb")
        emprestimos = pickle.load(pickle_in)
        pickle_in.close()
        pickle_in = open(config.getArquivoLivros(), "rb")
        livros = pickle.load(pickle_in)
        pickle_in.close()

        self.__biblio.restoreDatabase(usuarios, emprestimos, livros)
