# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NovoLivro.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CadastroLivro(object):
    def setupUi(self, CadastroLivro):
        CadastroLivro.setObjectName("CadastroLivro")
        CadastroLivro.resize(435, 320)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        CadastroLivro.setFont(font)
        self.novoLivroText = QtWidgets.QLabel(CadastroLivro)
        self.novoLivroText.setEnabled(True)
        self.novoLivroText.setGeometry(QtCore.QRect(30, 15, 211, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.novoLivroText.setFont(font)
        self.novoLivroText.setFocusPolicy(QtCore.Qt.NoFocus)
        self.novoLivroText.setTextFormat(QtCore.Qt.AutoText)
        self.novoLivroText.setObjectName("novoLivroText")
        self.tituloText = QtWidgets.QLabel(CadastroLivro)
        self.tituloText.setGeometry(QtCore.QRect(30, 110, 121, 16))
        self.tituloText.setObjectName("tituloText")
        self.tituloInput = QtWidgets.QLineEdit(CadastroLivro)
        self.tituloInput.setGeometry(QtCore.QRect(30, 130, 181, 21))
        self.tituloInput.setObjectName("tituloInput")
        self.codLivroText = QtWidgets.QLabel(CadastroLivro)
        self.codLivroText.setGeometry(QtCore.QRect(30, 60, 121, 16))
        self.codLivroText.setObjectName("codLivroText")
        self.codLivroInput = QtWidgets.QLineEdit(CadastroLivro)
        self.codLivroInput.setGeometry(QtCore.QRect(140, 50, 51, 31))
        self.codLivroInput.setObjectName("codLivroInput")
        self.anoText = QtWidgets.QLabel(CadastroLivro)
        self.anoText.setGeometry(QtCore.QRect(250, 110, 121, 16))
        self.anoText.setObjectName("anoText")
        self.anoInput = QtWidgets.QLineEdit(CadastroLivro)
        self.anoInput.setGeometry(QtCore.QRect(250, 130, 91, 21))
        self.anoInput.setText("")
        self.anoInput.setObjectName("anoInput")
        self.botaoEnviar = QtWidgets.QPushButton(CadastroLivro)
        self.botaoEnviar.setGeometry(QtCore.QRect(270, 200, 113, 32))
        self.botaoEnviar.setObjectName("botaoEnviar")

        self.retranslateUi(CadastroLivro)
        QtCore.QMetaObject.connectSlotsByName(CadastroLivro)

        #Controle de Inputs
        #Titulo
        regex=QtCore.QRegExp("[a-z-A-Z-0-9_. á-ú-Á-Ú]+")
        validator = QtGui.QRegExpValidator(regex)
        self.tituloInput.setValidator(validator)
        #Ano
        regex=QtCore.QRegExp("[0-9]+")
        validator = QtGui.QRegExpValidator(regex)
        self.anoInput.setValidator(validator)
        #Cod Livro
        regex=QtCore.QRegExp("[0-9]+")
        validator = QtGui.QRegExpValidator(regex)
        self.codLivroInput.setValidator(validator)

    def retranslateUi(self, CadastroLivro):
        _translate = QtCore.QCoreApplication.translate
        CadastroLivro.setWindowTitle(_translate("CadastroLivro", "Cadastro de Livro"))
        self.novoLivroText.setText(_translate("CadastroLivro", "Novo Livro"))
        self.tituloText.setText(_translate("CadastroLivro", "Título:"))
        self.tituloInput.setPlaceholderText(_translate("CadastroLivro", "Ex: Um Curso de Cálculo Vol 1"))
        self.codLivroText.setText(_translate("CadastroLivro", "Código do livro:"))
        self.codLivroInput.setPlaceholderText(_translate("CadastroLivro", "Ex: 923"))
        self.anoText.setText(_translate("CadastroLivro", "Ano:"))
        self.anoInput.setPlaceholderText(_translate("CadastroLivro", "Ex: 2018"))
        self.botaoEnviar.setText(_translate("CadastroLivro", "Enviar"))
