import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from principalUI import *
from NovoAluno import *
from NovoProfessor import *

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
        self.dialog.home()
        print("Janela de Cadastro de Aluno aberta!")

    #Quando selecionar a opção de menu (novo professor)
    def on_NovoProfessor_clicked(self):
        self.dialog = ProfessorWindow()
        self.dialog.home()
        print("Janela de Cadastro de Professor aberta!")


    def home(self):
        self.ui.startTable.horizontalHeader().setSectionResizeMode(1) #stretched table
        ##Colocando item na tabela inicial
        item = QtWidgets.QTableWidgetItem()
        item.setData(0, controlador.getNumEmprestimos()) #setData(Role, data) role = 1 é a displayRole, aqui sera adicionado o que deve ser apresentado na tabela
        self.ui.startTable.setItem(0, 1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setData(0, controlador.getNumEmprestimos()) #setData(Role, data) role = 1 é a displayRole, aqui sera adicionado o que deve ser apresentado na tabela
        self.ui.startTable.setItem(1, 1, item)

        ##Apertando botões do menu de cadastro
        self.ui.actionNovo_Aluno.triggered.connect(self.on_NovoAluno_clicked)    #Abre janela de cadastro de aluno
        self.ui.actionNovo_Professor.triggered.connect(self.on_NovoProfessor_clicked) #Abre a janela de cadastro de professor
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
        codUsuario = self.ui.codUsuarioInput.text()
        nome = self.ui.nomeUsuarioInput.text()
        curso = str(self.ui.cursoListBox.currentText())
        ano = self.ui.anoInput.text()
        #Cadastrando
        controlador.addAluno(codUsuario, nome, curso, ano)
        print("Cadastro Feito!")
        self.popup = QtWidgets.QMessageBox.warning(self, 'Nice!', "Cadastro feito com sucesso!", QtWidgets.QMessageBox.Ok)
        self.popup

    def home(self):
        #Logica do cadastro de ALUNO deve vir aqui
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
        codUsuario = self.ui.codUsuarioInput.text()
        nome = self.ui.nomeUsuarioInput.text()
        titulacao = self.ui.titulacaoInput.text()
        #Cadastrando
        controlador.addProfessor(codUsuario, nome, titulacao)
        print("Cadastro Feito!")
        self.popup = QtWidgets.QMessageBox.warning(self, 'Nice!', "Cadastro feito com sucesso!", QtWidgets.QMessageBox.Ok)
        self.popup


    def home(self):
        #Logica do cadastro de PROFESSOR deve vir aqui
        self.ui.botaoEnviar.clicked.connect(self.cadastroProfessor)
        self.show()



#Roda nossa UI
def run():
    app = QApplication(sys.argv)
    window = PrincipalWindow()
    sys.exit(app.exec_())

run()
