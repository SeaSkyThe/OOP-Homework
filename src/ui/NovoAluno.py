# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NovoAluno.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CadastroAluno(object):
    def setupUi(self, CadastroAluno):
        CadastroAluno.setObjectName("CadastroAluno")
        CadastroAluno.resize(458, 306)
        self.novoAlunoText = QtWidgets.QLabel(CadastroAluno)
        self.novoAlunoText.setEnabled(True)
        self.novoAlunoText.setGeometry(QtCore.QRect(30, 10, 211, 27))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.novoAlunoText.setFont(font)
        self.novoAlunoText.setTextFormat(QtCore.Qt.AutoText)
        self.novoAlunoText.setObjectName("novoAlunoText")
        self.codUsuarioText = QtWidgets.QLabel(CadastroAluno)
        self.codUsuarioText.setGeometry(QtCore.QRect(30, 60, 121, 16))
        self.codUsuarioText.setObjectName("codUsuarioText")
        self.codUsuarioInput = QtWidgets.QLineEdit(CadastroAluno)
        self.codUsuarioInput.setGeometry(QtCore.QRect(150, 50, 51, 31))
        self.codUsuarioInput.setObjectName("codUsuarioInput")
        self.nomeUsuarioText = QtWidgets.QLabel(CadastroAluno)
        self.nomeUsuarioText.setGeometry(QtCore.QRect(30, 100, 121, 16))
        self.nomeUsuarioText.setObjectName("nomeUsuarioText")
        self.nomeUsuarioInput = QtWidgets.QLineEdit(CadastroAluno)
        self.nomeUsuarioInput.setGeometry(QtCore.QRect(30, 120, 181, 21))
        self.nomeUsuarioInput.setObjectName("nomeUsuarioInput")
        self.cursoText = QtWidgets.QLabel(CadastroAluno)
        self.cursoText.setGeometry(QtCore.QRect(30, 150, 121, 16))
        self.cursoText.setObjectName("cursoText")
        self.cursoListBox = QtWidgets.QComboBox(CadastroAluno)
        self.cursoListBox.setGeometry(QtCore.QRect(30, 170, 191, 26))
        self.cursoListBox.setObjectName("cursoListBox")
        self.cursoListBox.addItem("")
        self.cursoListBox.addItem("")
        self.cursoListBox.addItem("")
        self.cursoListBox.addItem("")
        self.cursoListBox.addItem("")
        self.cursoListBox.addItem("")
        self.cursoListBox.addItem("")
        self.cursoListBox.addItem("")
        self.cursoListBox.addItem("")
        self.anoText = QtWidgets.QLabel(CadastroAluno)
        self.anoText.setGeometry(QtCore.QRect(240, 100, 121, 16))
        self.anoText.setObjectName("anoText")
        self.anoInput = QtWidgets.QLineEdit(CadastroAluno)
        self.anoInput.setGeometry(QtCore.QRect(240, 120, 91, 21))
        self.anoInput.setText("")
        self.anoInput.setObjectName("anoInput")
        self.botaoEnviar = QtWidgets.QPushButton(CadastroAluno)
        self.botaoEnviar.setGeometry(QtCore.QRect(290, 220, 113, 32))
        self.botaoEnviar.setObjectName("botaoEnviar")

        self.retranslateUi(CadastroAluno)
        QtCore.QMetaObject.connectSlotsByName(CadastroAluno)

        #Controle de Inputs
        #Nome
        regex=QtCore.QRegExp("[a-z-A-Z_ á-ú-Á-Ú]+")
        validator = QtGui.QRegExpValidator(regex)
        self.nomeUsuarioInput.setValidator(validator)
        #Cod Usuario
        regex=QtCore.QRegExp("[0-9]+")
        validator = QtGui.QRegExpValidator(regex)
        self.codUsuarioInput.setValidator(validator)
        #Ano
        regex=QtCore.QRegExp("[0-9]+")
        validator = QtGui.QRegExpValidator(regex)
        self.anoInput.setValidator(validator)

    def retranslateUi(self, CadastroAluno):
        _translate = QtCore.QCoreApplication.translate
        CadastroAluno.setWindowTitle(_translate("CadastroAluno", "Cadastro de Aluno"))
        self.novoAlunoText.setText(_translate("CadastroAluno", "Novo aluno"))
        self.codUsuarioText.setText(_translate("CadastroAluno", "Código de usuário:"))
        self.codUsuarioInput.setPlaceholderText(_translate("CadastroAluno", "Ex: 879"))
        self.nomeUsuarioText.setText(_translate("CadastroAluno", "Nome Completo:"))
        self.nomeUsuarioInput.setPlaceholderText(_translate("CadastroAluno", "Ex: Marcelo Eduardo"))
        self.cursoText.setText(_translate("CadastroAluno", "Curso:"))
        self.cursoListBox.setItemText(0, _translate("CadastroAluno", "Ciência da Computação"))
        self.cursoListBox.setItemText(1, _translate("CadastroAluno", "Engenharia Cartográfica"))
        self.cursoListBox.setItemText(2, _translate("CadastroAluno", "Geografia"))
        self.cursoListBox.setItemText(3, _translate("CadastroAluno", "Física"))
        self.cursoListBox.setItemText(4, _translate("CadastroAluno", "Química"))
        self.cursoListBox.setItemText(5, _translate("CadastroAluno", "Arquitetura e Urbanismo"))
        self.cursoListBox.setItemText(6, _translate("CadastroAluno", "Ed. Física"))
        self.cursoListBox.setItemText(7, _translate("CadastroAluno", "Fisioterapia"))
        self.cursoListBox.setItemText(8, _translate("CadastroAluno", "Matemática"))
        self.anoText.setText(_translate("CadastroAluno", "Ano:"))
        self.anoInput.setPlaceholderText(_translate("CadastroAluno", "Ex: 2018"))
        self.botaoEnviar.setText(_translate("CadastroAluno", "Enviar"))
