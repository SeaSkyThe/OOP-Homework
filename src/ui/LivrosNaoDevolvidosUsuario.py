# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LivrosNaoDevolvidosUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LivrosNaoDevolvidosUsuario(object):
    def setupUi(self, LivrosNaoDevolvidosUsuario):
        LivrosNaoDevolvidosUsuario.setObjectName("LivrosNaoDevolvidosUsuario")
        LivrosNaoDevolvidosUsuario.resize(561, 466)
        self.BigText = QtWidgets.QLabel(LivrosNaoDevolvidosUsuario)
        self.BigText.setGeometry(QtCore.QRect(20, 0, 591, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BigText.setFont(font)
        self.BigText.setObjectName("BigText")
        self.tabelaRelatorio = QtWidgets.QTableWidget(LivrosNaoDevolvidosUsuario)
        self.tabelaRelatorio.setGeometry(QtCore.QRect(20, 130, 511, 271))
        self.tabelaRelatorio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabelaRelatorio.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabelaRelatorio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabelaRelatorio.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabelaRelatorio.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabelaRelatorio.setDragEnabled(False)
        self.tabelaRelatorio.setObjectName("tabelaRelatorio")
        self.tabelaRelatorio.setColumnCount(4)
        self.tabelaRelatorio.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(3, item)
        self.tabelaRelatorio.horizontalHeader().setSortIndicatorShown(False)
        self.tabelaRelatorio.horizontalHeader().setStretchLastSection(False)
        self.pesquisarButton = QtWidgets.QPushButton(LivrosNaoDevolvidosUsuario)
        self.pesquisarButton.setGeometry(QtCore.QRect(420, 420, 113, 32))
        self.pesquisarButton.setObjectName("pesquisarButton")
        self.codUsuarioInput = QtWidgets.QLineEdit(LivrosNaoDevolvidosUsuario)
        self.codUsuarioInput.setGeometry(QtCore.QRect(20, 90, 141, 21))
        self.codUsuarioInput.setObjectName("codUsuarioInput")
        self.codUsuarioText = QtWidgets.QLabel(LivrosNaoDevolvidosUsuario)
        self.codUsuarioText.setGeometry(QtCore.QRect(20, 40, 411, 51))
        self.codUsuarioText.setObjectName("codUsuarioText")

        self.retranslateUi(LivrosNaoDevolvidosUsuario)
        QtCore.QMetaObject.connectSlotsByName(LivrosNaoDevolvidosUsuario)

        #Controle de inputs
        #Cod Usuario
        regex=QtCore.QRegExp("[0-9]+")
        validator = QtGui.QRegExpValidator(regex)
        self.codUsuarioInput.setValidator(validator)

    def retranslateUi(self, LivrosNaoDevolvidosUsuario):
        _translate = QtCore.QCoreApplication.translate
        LivrosNaoDevolvidosUsuario.setWindowTitle(_translate("LivrosNaoDevolvidosUsuario", "Livros não devolvidos por um usuário"))
        self.BigText.setText(_translate("LivrosNaoDevolvidosUsuario", "Livros não devolvidos por um usuário"))
        item = self.tabelaRelatorio.horizontalHeaderItem(0)
        item.setText(_translate("LivrosNaoDevolvidosUsuario", "Código"))
        item = self.tabelaRelatorio.horizontalHeaderItem(1)
        item.setText(_translate("LivrosNaoDevolvidosUsuario", "Título"))
        item = self.tabelaRelatorio.horizontalHeaderItem(2)
        item.setText(_translate("LivrosNaoDevolvidosUsuario", "Ano"))
        item = self.tabelaRelatorio.horizontalHeaderItem(3)
        item.setText(_translate("LivrosNaoDevolvidosUsuario", "Atrasado"))
        self.pesquisarButton.setText(_translate("LivrosNaoDevolvidosUsuario", "Pesquisar"))
        self.codUsuarioText.setText(_translate("LivrosNaoDevolvidosUsuario", "Código do Usuário"))
