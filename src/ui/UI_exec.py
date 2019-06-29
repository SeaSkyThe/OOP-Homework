import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtCore import QTimer
from principalUI import *
from NovoAluno import *
from NovoProfessor import *
from NovoLivro import *
from NovoEmprestimo import *
from RelatorioUsuarios import *
from RelatorioAlunos import *
from RelatorioProfessores import *
from RelatorioLivros import *
from LivrosDisponiveis import *
from LivrosEmprestados import *

del sys.path[0]
sys.path.insert(0, '..')
from controlador.Controlador import *



controlador = Controlador()

class PrincipalWindow(QMainWindow):  #Main window
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.home()

        self.dialogs = list()

        #Refresh na tela inicial para atualização da tabela
        self.Timer = QTimer()
        self.Timer.setInterval(1000)
        self.Timer.timeout.connect(self.setItemsInTable)
        self.Timer.start()

    #Quando apertar o botao de novo emprestimo
    def on_NovoEmprestimo_clicked(self):
        self.dialog = EmprestimoWindow()
        print("Janela de Emprestimo aberta!")
    #Quando selecionar a opção de menu (novo aluno)
    def on_NovoAluno_clicked(self):
        self.dialog = AlunoWindow()
        #self.dialog.home()  isso ja é chamado na função AlunoWindow() - colocar isso aqui tava dando duplo envio de sinal no botao
        print("Janela de Cadastro de Aluno aberta!")

    #Quando selecionar a opção de menu (novo professor)
    def on_NovoProfessor_clicked(self):
        self.dialog = ProfessorWindow()
        #self.dialog.home() isso ja é chamado na função ProfessorWindow() -  colocar isso aqui tava dando duplo envio de sinal no botao
        print("Janela de Cadastro de Professor aberta!")

    def on_NovoLivro_clicked(self):
        self.dialog = LivroWindow()
        print("Janela de Cadastro de Livro aberta!")

    #Quando selecionar opção de menu de relatorio
    def on_TodosUsuarios_clicked(self):
        self.dialog = RelatorioUsuarios()
        print("Janela de Relatorio de Usuarios aberta!")

    def on_TodosAlunos_clicked(self):
        self.dialog = RelatorioAlunos()
        print("Janela de Relatorio de Alunos aberta!")

    def on_TodosProfessores_clicked(self):
        self.dialog = RelatorioProfessores()
        print("Janela de Relatorio de Professores aberta!")

    def on_TodosLivros_clicked(self):
        self.dialog = RelatorioLivros()
        print("Janela de Relatorio de Livros aberta!")

    def on_LivrosDisponiveis_clicked(self):
        self.dialog = LivrosDisponiveis()
        print("Janela de Relatorio de Livros Disponiveis aberta!")

    def on_LivrosEmprestados_clicked(self):
        self.dialog = LivrosEmprestados()
        print("Janela de Relatorio de Livros Emprestados aberta!")

    def on_SalvarDados_clicked(self):
        controlador.saveAll()
        print("Chamando funcao de salvamento")
        self.popup = QtWidgets.QMessageBox.warning(self, 'Nice!', "Dados salvos com sucesso!", QtWidgets.QMessageBox.Ok)

    def on_CarregarDados_clicked(self):
        controlador.loadData()
        print("Chamando funcao de carregamento")
        self.popup = QtWidgets.QMessageBox.warning(self, 'Nice!', "Dados recuperados com sucesso! Bom trabalho :)", QtWidgets.QMessageBox.Ok)

    def setItemsInTable(self):
        ##Colocando item na tabela inicial
        item = QtWidgets.QTableWidgetItem()
        numEmprestimos = controlador.getNumEmprestimos()
        item.setData(0, numEmprestimos) #setData(Role, data) role = 0 é a displayRole, aqui sera adicionado o que deve ser apresentado na tabela
        self.ui.startTable.setItem(0, 1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setData(0, controlador.getNumAtrasos()) #setData(Role, data) role = 0 é a displayRole, aqui sera adicionado o que deve ser apresentado na tabela
        self.ui.startTable.setItem(1, 1, item)


    def home(self):
        self.ui.startTable.horizontalHeader().setSectionResizeMode(1) #stretched table

        self.setItemsInTable()
        ##Apertando botões do menu de cadastro de Aluno e Professor e de livro
        self.ui.actionNovo_Aluno.triggered.connect(self.on_NovoAluno_clicked)    #Abre janela de cadastro de aluno
        self.ui.actionNovo_Professor.triggered.connect(self.on_NovoProfessor_clicked) #Abre a janela de cadastro de professor
        self.ui.actionNovo_Livro.triggered.connect(self.on_NovoLivro_clicked) #Abre janela de cadastro de livro
        ##Menus de relatorio
        self.ui.actionTodos_os_usuarios.triggered.connect(self.on_TodosUsuarios_clicked)
        self.ui.actionTodos_os_alunos.triggered.connect(self.on_TodosAlunos_clicked)
        self.ui.actionTodos_os_professores.triggered.connect(self.on_TodosProfessores_clicked)
        self.ui.actionTodos_os_livros.triggered.connect(self.on_TodosLivros_clicked)
        self.ui.actionLivros_disponiveis.triggered.connect(self.on_LivrosDisponiveis_clicked)
        self.ui.actionLivros_emprestados.triggered.connect(self.on_LivrosEmprestados_clicked)

        ##Menu de novo Emprestimo
        self.ui.buttonEmprestimo.clicked.connect(self.on_NovoEmprestimo_clicked)
        ## SALVAMENTO E CARREGAMENTO DE DADOS
        self.ui.actionSalvar_Dados.triggered.connect(self.on_SalvarDados_clicked)
        self.ui.actionCarregar_Dados.triggered.connect(self.on_CarregarDados_clicked)


        #mostrando interface
        self.show()


########################################################## EMPRÉSTIMO ####################################################################
class EmprestimoWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_NovoEmprestimo()
        self.ui.setupUi(self)
        self.home()
        self.livrosEmprestar = []

    def fillUserBox(self):
        usuarios = controlador.getUsuarios()
        for usuario in usuarios:
            nomeUsuario = usuario.getNome()
            self.ui.selectUser.addItem(nomeUsuario)

    def fillBookBox(self):
        livros = controlador.getLivros()
        for livro in livros:
            if(livro.estaEmprestado() == False):
                nomeLivro = livro.getNome()
                self.ui.selectBook.addItem(nomeLivro)

    def putItemInTable(self):
        #Logica para exibição na tabela
        nomeLivro = self.ui.selectBook.currentText()
        livro = controlador.getLivroNome(nomeLivro)
        if(livro != None and livro.estaEmprestado() == False):
            rowPosition = self.ui.tabelaLivrosEmprestimo.rowCount()
            self.ui.tabelaLivrosEmprestimo.insertRow(rowPosition)

            item = QtWidgets.QTableWidgetItem()
            codigoLivro = livro.getCodLivro()
            item.setData(0, codigoLivro)
            self.ui.tabelaLivrosEmprestimo.setItem(rowPosition, 0, item)

            nomeLivro = livro.getNome()
            item = QtWidgets.QTableWidgetItem()
            item.setData(0, nomeLivro)
            self.ui.tabelaLivrosEmprestimo.setItem(rowPosition, 1, item)

            anoLivro = livro.getAno()
            item = QtWidgets.QTableWidgetItem()
            item.setData(0, anoLivro)
            self.ui.tabelaLivrosEmprestimo.setItem(rowPosition, 2, item)
        else:
            self.popup = QtWidgets.QMessageBox.warning(self, 'Oops!', "Esse livro está emprestado", QtWidgets.QMessageBox.Ok)
            self.show()

        self.livrosEmprestar.append(livro)
        self.ui.tabelaLivrosEmprestimo.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def onFazerEmprestimoClicked(self):
        if(len(self.ui.codEmprestimoInput.text()) > 0 and self.ui.tabelaLivrosEmprestimo.rowCount() > 0):
            codEmprestimo = self.ui.codEmprestimoInput.text()
            usuario = controlador.getUsuarioNome(self.ui.selectUser.currentText())
            controlador.addEmprestimo(codEmprestimo, usuario)
            controlador.addItensEmprestimo(codEmprestimo, self.livrosEmprestar)
            self.popup = QtWidgets.QMessageBox.warning(self, 'Nice!', "Empréstimo realizado com sucesso!", QtWidgets.QMessageBox.Ok)
            self.popup
        else:
            self.popup = QtWidgets.QMessageBox.warning(self, 'Oops!', "Por favor, verifique se preencheu o campo de codigo de empréstimo e selecionou ao menos um livro!", QtWidgets.QMessageBox.Ok)
            self.show()

    def home(self):
        self.fillUserBox()
        self.fillBookBox()
        self.ui.addBook.clicked.connect(self.putItemInTable)
        self.ui.finalizarEmprestimo.clicked.connect(self.onFazerEmprestimoClicked)
        self.show()

######################################################### CADASTROS ####################################################################
#Janela de cadastro de Aluno
class AlunoWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CadastroAluno()
        self.ui.setupUi(self)
        self.home()

    def cadastroAluno(self):
        if(len(self.ui.codUsuarioInput.text()) > 0 and len(self.ui.nomeUsuarioInput.text()) > 0 and len(self.ui.anoInput.text())):
            #Logica do cadastro de ALUNO deve vir aqui
            if(controlador.getUsuarioCodigo(self.ui.codUsuarioInput.text()) == None):
                self.__codUsuario = self.ui.codUsuarioInput.text()
                self.__nome = self.ui.nomeUsuarioInput.text()
                self.__curso = str(self.ui.cursoListBox.currentText())
                self.__ano = self.ui.anoInput.text()

                #Cadastrando - Pode-se colocar verificação de erros aqui
                controlador.addAluno(self.__codUsuario, self.__nome, self.__curso, self.__ano)
                print("Cadastro de Aluno Feito!")
                #Janela de aviso
                self.popup = QtWidgets.QMessageBox.warning(self, 'Nice!', "Cadastro feito com sucesso!", QtWidgets.QMessageBox.Ok)
                self.popup
                #clear campos
                self.ui.codUsuarioInput.setText("")
                self.ui.nomeUsuarioInput.setText("")
                self.ui.anoInput.setText("")

            else:
                self.popup = QtWidgets.QMessageBox.warning(self, 'Oops!', "Já existe um usuário cadastrado com esse código! Tente novamente!", QtWidgets.QMessageBox.Ok)
                self.show()

        else:
            self.popup = QtWidgets.QMessageBox.warning(self, 'Oops!', "Por favor preencha todos os campos", QtWidgets.QMessageBox.Ok)
            self.show()

    def home(self):
        #Logica do cadastro de ALUNO prossegue aqui
        #Exemplo: Quando botao for clicado, pegar input do nome e imprimir (funcao: getNomeInput) acima:
        self.ui.botaoEnviar.clicked.connect(self.cadastroAluno) #apenas referencie o metodo, nao chame-o
        self.show()


#Janela de Cadastro de Professor
class ProfessorWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CadastroProfessor()
        self.ui.setupUi(self)
        self.home()

    def cadastroProfessor(self):
        #Logica do cadastro de PROFESSOR deve vir aqui
        if(len(self.ui.codUsuarioInput.text()) > 0 and len(self.ui.nomeUsuarioInput.text()) > 0 and len(self.ui.titulacaoInput.text()) > 0):
            if(controlador.getUsuarioCodigo(self.ui.codUsuarioInput.text()) == None):
                self.__codUsuario = self.ui.codUsuarioInput.text()
                self.__nome = self.ui.nomeUsuarioInput.text()
                self.__titulacao = self.ui.titulacaoInput.text()
                #Cadastrando - Pode-se colocar verificação de erros aqui
                controlador.addProfessor(self.__codUsuario, self.__nome, self.__titulacao)
                print("Cadastro de Professor Feito!")
                #Janela de aviso
                self.popup = QtWidgets.QMessageBox.warning(self, 'Nice!', "Cadastro feito com sucesso!", QtWidgets.QMessageBox.Ok)
                #clear campos
                self.ui.codUsuarioInput.setText("")
                self.ui.nomeUsuarioInput.setText("")
                self.ui.titulacaoInput.setText("")
            else:
                self.popup = QtWidgets.QMessageBox.warning(self, 'Oops!', "Já existe um usuário cadastrado com esse código! Tente novamente!", QtWidgets.QMessageBox.Ok)
                self.show()
        else:
            self.popup = QtWidgets.QMessageBox.warning(self, 'Oops!', "Por favor preencha todos os campos", QtWidgets.QMessageBox.Ok)
            print("Aviso sobre campos dado.")
            self.show()

    def home(self):
        #Logica do cadastro de PROFESSOR prossegue aqui
        self.ui.botaoEnviar.clicked.connect(self.cadastroProfessor)
        self.show()


#Janela de Cadastro de Livro
class LivroWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CadastroLivro()
        self.ui.setupUi(self)
        self.home()

    def cadastroLivro(self):
        if(len(self.ui.codLivroInput.text()) > 0 and len(self.ui.tituloInput.text()) > 0 and len(self.ui.anoInput.text()) > 0):
            if(controlador.getLivroCodigo(self.ui.codLivroInput.text()) == None):
                #Logica de cadastro de LIVRO vem aqui
                self.__codLivro = self.ui.codLivroInput.text()
                self.__titulo = self.ui.tituloInput.text()
                self.__ano = self.ui.anoInput.text()
                #Cadastrando - Pode-se colocar verificação de erros aqui
                controlador.addLivro(self.__codLivro, self.__titulo, self.__ano)
                print("Cadastro de Livro Feito!")
                #Janela de aviso
                self.popup = QtWidgets.QMessageBox.warning(self, 'Nice!', "Cadastro feito com sucesso!", QtWidgets.QMessageBox.Ok)
            else:
                self.popup = QtWidgets.QMessageBox.warning(self, 'Oops!', "Já existe um livro cadastrado com esse código! Tente novamente!", QtWidgets.QMessageBox.Ok)
                self.show()

        else:
            self.popup = QtWidgets.QMessageBox.warning(self, 'Oops!', "Por favor preencha todos os campos", QtWidgets.QMessageBox.Ok)
            print("Aviso sobre campos dado.")
            self.show()

    def home(self):
        self.ui.botaoEnviar.clicked.connect(self.cadastroLivro) #referencia o metodo, nao chame-o
        self.show()

######################################################### RELATORIOS ####################################################################
#Janela de Relatorio de Todos os Usuarios
class RelatorioUsuarios(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RelatorioUsuarios()
        self.ui.setupUi(self)
        self.home()

    def fillTable(self):
        #Logica para exibição na tabela, tem que ver se o acesso não está sendo muito direto, e deveriamos acessar o conteudo do usuario pelo controlador
        usuarios = controlador.getUsuarios()
        for each in usuarios:
            rowPosition = self.ui.tabelaRelatorio.rowCount()
            self.ui.tabelaRelatorio.insertRow(rowPosition)

            item = QtWidgets.QTableWidgetItem()

            codigoUsuario = each.getCodUsuario()
            item.setData(0, codigoUsuario)
            self.ui.tabelaRelatorio.setItem(rowPosition, 0, item)

            nomeUsuario = each.getNome()
            item = QtWidgets.QTableWidgetItem()
            item.setData(0, nomeUsuario)
            self.ui.tabelaRelatorio.setItem(rowPosition, 1, item)


            #aqui vai ter que verificar se existe item atrasado(NECESSARIO FAZER)
            item = QtWidgets.QTableWidgetItem()
            isAtrasado = controlador.UsuarioComAtraso(each)
            if(isAtrasado == True):
                item.setData(0, "Sim")
            else:
                item.setData(0, "Não")
            self.ui.tabelaRelatorio.setItem(rowPosition, 2, item)

            #aqui a logica para colocar na tabela se o usuario tem livros para devolver
            item = QtWidgets.QTableWidgetItem()
            isEmprestado = controlador.UsuarioComEmprestimo(each)
            if(isEmprestado == True):
                item.setData(0, "Sim")
            else:
                item.setData(0, "Não")
            self.ui.tabelaRelatorio.setItem(rowPosition, 3, item)

    def home(self):
        self.ui.tabelaRelatorio.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fillTable()
        self.show()

#Janela de Relatorio de Todos os Alunos
class RelatorioAlunos(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RelatorioAlunos()
        self.ui.setupUi(self)
        self.home()

    def fillTable(self):
        #Logica para exibição na tabela
        alunos = controlador.getAlunos()
        for each in alunos:
            rowPosition = self.ui.tabelaRelatorio.rowCount()
            self.ui.tabelaRelatorio.insertRow(rowPosition)

            item = QtWidgets.QTableWidgetItem()

            codigoUsuario = each.getCodUsuario()
            item.setData(0, codigoUsuario)
            self.ui.tabelaRelatorio.setItem(rowPosition, 0, item)

            nomeUsuario = each.getNome()
            item = QtWidgets.QTableWidgetItem()
            item.setData(0, nomeUsuario)
            self.ui.tabelaRelatorio.setItem(rowPosition, 1, item)


            #aqui vai ter que verificar se existe item atrasado(NECESSARIO FAZER)
            item = QtWidgets.QTableWidgetItem()
            isAtrasado = controlador.UsuarioComAtraso(each)
            if(isAtrasado == True):
                item.setData(0, "Sim")
            else:
                item.setData(0, "Não")
            self.ui.tabelaRelatorio.setItem(rowPosition, 2, item)

            #aqui a logica para colocar na tabela se o usuario tem livros para devolver
            item = QtWidgets.QTableWidgetItem()
            isEmprestado = controlador.UsuarioComEmprestimo(each)
            if(isEmprestado == True):
                item.setData(0, "Sim")
            else:
                item.setData(0, "Não")
            self.ui.tabelaRelatorio.setItem(rowPosition, 3, item)

    def home(self):
        self.ui.tabelaRelatorio.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fillTable()
        self.show()

#Janela de Relatorio de Todos os Professores
class RelatorioProfessores(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RelatorioProfessores()
        self.ui.setupUi(self)
        self.home()

    def fillTable(self):
        #Logica para exibição na tabela
        professores = controlador.getProfessores()
        for each in professores:
            rowPosition = self.ui.tabelaRelatorio.rowCount()
            self.ui.tabelaRelatorio.insertRow(rowPosition)

            item = QtWidgets.QTableWidgetItem()

            codigoUsuario = each.getCodUsuario()
            item.setData(0, codigoUsuario)
            self.ui.tabelaRelatorio.setItem(rowPosition, 0, item)

            nomeUsuario = each.getNome()
            item = QtWidgets.QTableWidgetItem()
            item.setData(0, nomeUsuario)
            self.ui.tabelaRelatorio.setItem(rowPosition, 1, item)



            item = QtWidgets.QTableWidgetItem()
            #aqui vai ter que verificar se existe item atrasado
            isAtrasado = controlador.UsuarioComAtraso(each)
            if(isAtrasado == True):
                item.setData(0, "Sim")
            else:
                item.setData(0, "Não")
            self.ui.tabelaRelatorio.setItem(rowPosition, 2, item)


            item = QtWidgets.QTableWidgetItem()
            #aqui a logica para colocar na tabela se o usuario tem livros para devolver
            isEmprestado = controlador.UsuarioComEmprestimo(each)
            if(isEmprestado == True):
                item.setData(0, "Sim")
            else:
                item.setData(0, "Não")
            self.ui.tabelaRelatorio.setItem(rowPosition, 3, item)


    def home(self):
        self.ui.tabelaRelatorio.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fillTable()
        self.show()

#Janela de Relatorio de Todos os Livros
class RelatorioLivros(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RelatorioLivros()
        self.ui.setupUi(self)
        self.home()

    def fillTable(self):
        #Logica para exibição na tabela
        livros = controlador.getLivros()
        for each in livros:
            rowPosition = self.ui.tabelaRelatorio.rowCount()
            self.ui.tabelaRelatorio.insertRow(rowPosition)

            item = QtWidgets.QTableWidgetItem()

            codLivro = each.getCodLivro()
            item.setData(0, codLivro)
            self.ui.tabelaRelatorio.setItem(rowPosition, 0, item)

            nomeLivro = each.getNome()
            item = QtWidgets.QTableWidgetItem()
            item.setData(0, nomeLivro)
            self.ui.tabelaRelatorio.setItem(rowPosition, 1, item)

            anoLivro = each.getAno()
            item = QtWidgets.QTableWidgetItem()
            item.setData(0, anoLivro)
            self.ui.tabelaRelatorio.setItem(rowPosition, 2, item)

            #Verifica se está emprestado
            item = QtWidgets.QTableWidgetItem()
            isEmprestado = controlador.livroEstaEmprestado(each)
            if(isEmprestado == True):
                item.setData(0, "Sim")
            else:
                item.setData(0, "Não")
            self.ui.tabelaRelatorio.setItem(rowPosition, 3, item)

            #AQUI TEM QUE VIR A LOGICA PARA VERIFICAR SE O LIVRO ESTÁ ATRASADO
            item = QtWidgets.QTableWidgetItem()
            isAtrasado = controlador.livroEstaAtrasado(each)
            if(isAtrasado == True):
                item.setData(0, "Sim")
            else:
                item.setData(0, "Não")
            self.ui.tabelaRelatorio.setItem(rowPosition, 4, item)
        pass

    def home(self):
        self.ui.tabelaRelatorio.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fillTable()
        self.show()


class LivrosDisponiveis(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LivrosDisponiveis()
        self.ui.setupUi(self)
        self.home()

    def fillTable(self):
        livros = controlador.getLivros()

        for each in livros:
            if(controlador.livroEstaEmprestado(each) == False):
                rowPosition = self.ui.tabelaRelatorio.rowCount()
                self.ui.tabelaRelatorio.insertRow(rowPosition)

                item = QtWidgets.QTableWidgetItem()

                codLivro = each.getCodLivro()
                item.setData(0, codLivro)
                self.ui.tabelaRelatorio.setItem(rowPosition, 0, item)

                nomeLivro = each.getNome()
                item = QtWidgets.QTableWidgetItem()
                item.setData(0, nomeLivro)
                self.ui.tabelaRelatorio.setItem(rowPosition, 1, item)

                anoLivro = each.getAno()
                item = QtWidgets.QTableWidgetItem()
                item.setData(0, anoLivro)
                self.ui.tabelaRelatorio.setItem(rowPosition, 2, item)

    def home(self):
        self.ui.tabelaRelatorio.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fillTable()
        self.show()

class LivrosEmprestados(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LivrosEmprestados()
        self.ui.setupUi(self)
        self.home()

    def fillTable(self):
        livros = controlador.getLivros()
        for each in livros:
            if(controlador.livroEstaEmprestado(each) == True):
                rowPosition = self.ui.tabelaRelatorio.rowCount()
                self.ui.tabelaRelatorio.insertRow(rowPosition)

                item = QtWidgets.QTableWidgetItem()

                codLivro = each.getCodLivro()
                item.setData(0, codLivro)
                self.ui.tabelaRelatorio.setItem(rowPosition, 0, item)

                nomeLivro = each.getNome()
                item = QtWidgets.QTableWidgetItem()
                item.setData(0, nomeLivro)
                self.ui.tabelaRelatorio.setItem(rowPosition, 1, item)

                anoLivro = each.getAno()
                item = QtWidgets.QTableWidgetItem()
                item.setData(0, anoLivro)
                self.ui.tabelaRelatorio.setItem(rowPosition, 2, item)

    def home(self):
        self.ui.tabelaRelatorio.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.fillTable()
        self.show()

#Roda nossa UI
def run():
    app = QApplication(sys.argv)
    window = PrincipalWindow()
    sys.exit(app.exec_())

#TESTS BEFORE RUN
controlador.addProfessor(144,"Danilo Eler", "Doutor")
controlador.addAluno (145, "Marcelo Eduardo Rodrigues", "Ciencia da Computacao", "2016")
controlador.addLivro(146, "Um curso de calculo vol 2", "2002")
run()
