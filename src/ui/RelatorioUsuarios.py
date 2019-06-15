# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RelatorioUsuarios.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RelatorioUsuarios(object):
    def setupUi(self, RelatorioUsuarios):
        RelatorioUsuarios.setObjectName("RelatorioUsuarios")
        RelatorioUsuarios.resize(505, 350)
        self.BigText = QtWidgets.QLabel(RelatorioUsuarios)
        self.BigText.setGeometry(QtCore.QRect(30, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BigText.setFont(font)
        self.BigText.setObjectName("BigText")
        self.tabelaRelatorio = QtWidgets.QTableWidget(RelatorioUsuarios)
        self.tabelaRelatorio.setGeometry(QtCore.QRect(40, 70, 411, 231))
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
        self.tabelaRelatorio.horizontalHeader().setStretchLastSection(True)

        self.retranslateUi(RelatorioUsuarios)
        QtCore.QMetaObject.connectSlotsByName(RelatorioUsuarios)

    def retranslateUi(self, RelatorioUsuarios):
        _translate = QtCore.QCoreApplication.translate
        RelatorioUsuarios.setWindowTitle(_translate("RelatorioUsuarios", "Dialog"))
        self.BigText.setText(_translate("RelatorioUsuarios", "Todos os Usuários"))
        item = self.tabelaRelatorio.horizontalHeaderItem(0)
        item.setText(_translate("RelatorioUsuarios", "Cod de Usuário"))
        item = self.tabelaRelatorio.horizontalHeaderItem(1)
        item.setText(_translate("RelatorioUsuarios", "Nome"))
        item = self.tabelaRelatorio.horizontalHeaderItem(2)
        item.setText(_translate("RelatorioUsuarios", "Livro atrasado"))
        item = self.tabelaRelatorio.horizontalHeaderItem(3)
        item.setText(_translate("RelatorioUsuarios", "Livro p/ devolver"))

