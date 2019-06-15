# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RelatorioAlunos.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RelatorioAlunos(object):
    def setupUi(self, RelatorioAlunos):
        RelatorioAlunos.setObjectName("RelatorioAlunos")
        RelatorioAlunos.resize(515, 359)
        self.BigText = QtWidgets.QLabel(RelatorioAlunos)
        self.BigText.setGeometry(QtCore.QRect(40, 40, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BigText.setFont(font)
        self.BigText.setObjectName("BigText")
        self.tabelaRelatorio = QtWidgets.QTableWidget(RelatorioAlunos)
        self.tabelaRelatorio.setGeometry(QtCore.QRect(40, 80, 401, 231))
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

        self.retranslateUi(RelatorioAlunos)
        QtCore.QMetaObject.connectSlotsByName(RelatorioAlunos)

    def retranslateUi(self, RelatorioAlunos):
        _translate = QtCore.QCoreApplication.translate
        RelatorioAlunos.setWindowTitle(_translate("RelatorioAlunos", "Dialog"))
        self.BigText.setText(_translate("RelatorioAlunos", "Todos os Alunos"))
        item = self.tabelaRelatorio.horizontalHeaderItem(0)
        item.setText(_translate("RelatorioAlunos", "Cod de Usuário"))
        item = self.tabelaRelatorio.horizontalHeaderItem(1)
        item.setText(_translate("RelatorioAlunos", "Nome"))
        item = self.tabelaRelatorio.horizontalHeaderItem(2)
        item.setText(_translate("RelatorioAlunos", "Livro atrasado"))
        item = self.tabelaRelatorio.horizontalHeaderItem(3)
        item.setText(_translate("RelatorioAlunos", "Livro p/ devolver"))

