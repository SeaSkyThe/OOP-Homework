# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HistoricoUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HistoricoUsuario(object):
    def setupUi(self, HistoricoUsuario):
        HistoricoUsuario.setObjectName("HistoricoUsuario")
        HistoricoUsuario.resize(552, 464)
        self.BigText = QtWidgets.QLabel(HistoricoUsuario)
        self.BigText.setGeometry(QtCore.QRect(20, 0, 591, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BigText.setFont(font)
        self.BigText.setObjectName("BigText")
        self.tabelaRelatorio = QtWidgets.QTableWidget(HistoricoUsuario)
        self.tabelaRelatorio.setGeometry(QtCore.QRect(20, 130, 511, 271))
        self.tabelaRelatorio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabelaRelatorio.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabelaRelatorio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabelaRelatorio.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabelaRelatorio.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabelaRelatorio.setDragEnabled(False)
        self.tabelaRelatorio.setObjectName("tabelaRelatorio")
        self.tabelaRelatorio.setColumnCount(3)
        self.tabelaRelatorio.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(2, item)
        self.tabelaRelatorio.horizontalHeader().setSortIndicatorShown(False)
        self.tabelaRelatorio.horizontalHeader().setStretchLastSection(False)
        self.pesquisarButton = QtWidgets.QPushButton(HistoricoUsuario)
        self.pesquisarButton.setGeometry(QtCore.QRect(420, 420, 113, 32))
        self.pesquisarButton.setObjectName("pesquisarButton")
        self.codUsuarioText = QtWidgets.QLabel(HistoricoUsuario)
        self.codUsuarioText.setGeometry(QtCore.QRect(20, 50, 411, 51))
        self.codUsuarioText.setObjectName("codUsuarioText")
        self.codUsuarioInput = QtWidgets.QLineEdit(HistoricoUsuario)
        self.codUsuarioInput.setGeometry(QtCore.QRect(20, 90, 141, 21))
        self.codUsuarioInput.setObjectName("codUsuarioInput")

        self.retranslateUi(HistoricoUsuario)
        QtCore.QMetaObject.connectSlotsByName(HistoricoUsuario)

    def retranslateUi(self, HistoricoUsuario):
        _translate = QtCore.QCoreApplication.translate
        HistoricoUsuario.setWindowTitle(_translate("HistoricoUsuario", "Histórico de um usuário"))
        self.BigText.setText(_translate("HistoricoUsuario", "Histórico do usuário"))
        item = self.tabelaRelatorio.horizontalHeaderItem(0)
        item.setText(_translate("HistoricoUsuario", "Código"))
        item = self.tabelaRelatorio.horizontalHeaderItem(1)
        item.setText(_translate("HistoricoUsuario", "Título"))
        item = self.tabelaRelatorio.horizontalHeaderItem(2)
        item.setText(_translate("HistoricoUsuario", "Ano"))
        self.pesquisarButton.setText(_translate("HistoricoUsuario", "Pesquisar"))
        self.codUsuarioText.setText(_translate("HistoricoUsuario", "Código do Usuário:"))

