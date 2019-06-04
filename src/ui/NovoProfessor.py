# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NovoProfessor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CadastroProfessor(object):
    def setupUi(self, CadastroProfessor):
        CadastroProfessor.setObjectName("CadastroProfessor")
        CadastroProfessor.resize(458, 306)
        self.novoProfessorText = QtWidgets.QLabel(CadastroProfessor)
        self.novoProfessorText.setEnabled(True)
        self.novoProfessorText.setGeometry(QtCore.QRect(30, 20, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.novoProfessorText.setFont(font)
        self.novoProfessorText.setTextFormat(QtCore.Qt.AutoText)
        self.novoProfessorText.setObjectName("novoProfessorText")
        self.codUsuarioText = QtWidgets.QLabel(CadastroProfessor)
        self.codUsuarioText.setGeometry(QtCore.QRect(30, 60, 121, 16))
        self.codUsuarioText.setObjectName("codUsuarioText")
        self.codUsuarioInput = QtWidgets.QLineEdit(CadastroProfessor)
        self.codUsuarioInput.setGeometry(QtCore.QRect(150, 50, 51, 31))
        self.codUsuarioInput.setObjectName("codUsuarioInput")
        self.nomeUsuarioText = QtWidgets.QLabel(CadastroProfessor)
        self.nomeUsuarioText.setGeometry(QtCore.QRect(30, 100, 121, 16))
        self.nomeUsuarioText.setObjectName("nomeUsuarioText")
        self.nomeUsuarioInput = QtWidgets.QLineEdit(CadastroProfessor)
        self.nomeUsuarioInput.setGeometry(QtCore.QRect(30, 120, 181, 21))
        self.nomeUsuarioInput.setObjectName("nomeUsuarioInput")
        self.anoText = QtWidgets.QLabel(CadastroProfessor)
        self.anoText.setGeometry(QtCore.QRect(240, 100, 121, 16))
        self.anoText.setObjectName("anoText")
        self.titulacaoInput = QtWidgets.QLineEdit(CadastroProfessor)
        self.titulacaoInput.setGeometry(QtCore.QRect(240, 120, 113, 21))
        self.titulacaoInput.setObjectName("titulacaoInput")
        self.botaoEnviar = QtWidgets.QPushButton(CadastroProfessor)
        self.botaoEnviar.setGeometry(QtCore.QRect(290, 220, 113, 32))
        self.botaoEnviar.setObjectName("botaoEnviar")

        self.retranslateUi(CadastroProfessor)
        QtCore.QMetaObject.connectSlotsByName(CadastroProfessor)

    def retranslateUi(self, CadastroProfessor):
        _translate = QtCore.QCoreApplication.translate
        CadastroProfessor.setWindowTitle(_translate("CadastroProfessor", "Cadastro de Professor"))
        self.novoProfessorText.setText(_translate("CadastroProfessor", "Novo Professor"))
        self.codUsuarioText.setText(_translate("CadastroProfessor", "Código de usuário:"))
        self.codUsuarioInput.setPlaceholderText(_translate("CadastroProfessor", "Ex: 923"))
        self.nomeUsuarioText.setText(_translate("CadastroProfessor", "Nome Completo:"))
        self.nomeUsuarioInput.setPlaceholderText(_translate("CadastroProfessor", "Ex: Danilo Eler"))
        self.anoText.setText(_translate("CadastroProfessor", "Titulação:"))
        self.titulacaoInput.setPlaceholderText(_translate("CadastroProfessor", "Doutor"))
        self.botaoEnviar.setText(_translate("CadastroProfessor", "Enviar"))

