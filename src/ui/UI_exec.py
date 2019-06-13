import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from principalUI import *
from NovoAluno import *
from NovoProfessor import *
from NovoLivro import *


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


    def home(self):
        self.ui.startTable.horizontalHeader().setSectionResizeMode(1) #stretched table
        ##Colocando item na tabela inicial
        item = QtWidgets.QTableWidgetItem()
        item.setData(0, 'Num Emprestimos') #setData(Role, data) role = 0 é a displayRole, aqui sera adicionado o que deve ser apresentado na tabela
        self.ui.startTable.setItem(0, 1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setData(0, 'Num Atrasos') #setData(Role, data) role = 0 é a displayRole, aqui sera adicionado o que deve ser apresentado na tabela
        self.ui.startTable.setItem(1, 1, item)

        ##Apertando botões do menu de cadastro de Aluno e Professor
        self.ui.actionNovo_Aluno.triggered.connect(self.on_NovoAluno_clicked)    #Abre janela de cadastro de aluno
        self.ui.actionNovo_Professor.triggered.connect(self.on_NovoProfessor_clicked) #Abre a janela de cadastro de professor

        ##Cadastro de livro
        self.ui.actionNovo_Livro.triggered.connect(self.on_NovoLivro_clicked) #Abre janela de cadastro de livro
        #mostrando interface
        self.show()

#Janela de cadastro de Aluno
class AlunoWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CadastroAluno()
        self.ui.setupUi(self)
        self.home()

    def cadastroAluno(self):
        #Logica do cadastro de ALUNO deve vir aqui
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
        self.__codUsuario = self.ui.codUsuarioInput.text()
        self.__nome = self.ui.nomeUsuarioInput.text()
        self.__titulacao = self.ui.titulacaoInput.text()
        #Cadastrando - Pode-se colocar verificação de erros aqui
        controlador.addProfessor(self.__codUsuario, self.__nome, self.__titulacao)
        print("Cadastro de Professor Feito!")
        #Janela de aviso
        self.popup = QtWidgets.QMessageBox.warning(self, 'Nice!', "Cadastro feito com sucesso!", QtWidgets.QMessageBox.Ok)
        self.popup


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
        #Logica de cadastro de LIVRO vem aqui
        self.__codLivro = self.ui.codLivroInput.text()
        self.__titulo = self.ui.tituloInput.text()
        self.__ano = self.ui.anoInput.text()
        #Cadastrando - Pode-se colocar verificação de erros aqui
        controlador.addLivro(self.__codLivro, self.__titulo, self.__ano)
        print("Cadastro de Livro Feito!")
        #Janela de aviso
        self.popup = QtWidgets.QMessageBox.warning(self, 'Nice!', "Cadastro feito com sucesso!", QtWidgets.QMessageBox.Ok)
        self.popup
    def home(self):
        self.ui.botaoEnviar.clicked.connect(self.cadastroLivro) #referencia o metodo, nao chame-o
        self.show()

#Roda nossa UI
def run():
    app = QApplication(sys.argv)
    window = PrincipalWindow()
    sys.exit(app.exec_())

run()
