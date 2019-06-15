# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RelatorioProfessores.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RelatorioProfessores(object):
    def setupUi(self, RelatorioProfessores):
        RelatorioProfessores.setObjectName("RelatorioProfessores")
        RelatorioProfessores.resize(511, 348)
        self.tabelaRelatorio = QtWidgets.QTableWidget(RelatorioProfessores)
        self.tabelaRelatorio.setGeometry(QtCore.QRect(40, 70, 431, 251))
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
        self.BigText = QtWidgets.QLabel(RelatorioProfessores)
        self.BigText.setGeometry(QtCore.QRect(40, 30, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BigText.setFont(font)
        self.BigText.setObjectName("BigText")

        self.retranslateUi(RelatorioProfessores)
        QtCore.QMetaObject.connectSlotsByName(RelatorioProfessores)

    def retranslateUi(self, RelatorioProfessores):
        _translate = QtCore.QCoreApplication.translate
        RelatorioProfessores.setWindowTitle(_translate("RelatorioProfessores", "Dialog"))
        item = self.tabelaRelatorio.horizontalHeaderItem(0)
        item.setText(_translate("RelatorioProfessores", "Cod de Usuário"))
        item = self.tabelaRelatorio.horizontalHeaderItem(1)
        item.setText(_translate("RelatorioProfessores", "Nome"))
        item = self.tabelaRelatorio.horizontalHeaderItem(2)
        item.setText(_translate("RelatorioProfessores", "Livro atrasado"))
        item = self.tabelaRelatorio.horizontalHeaderItem(3)
        item.setText(_translate("RelatorioProfessores", "Livro p/ devolver"))
        self.BigText.setText(_translate("RelatorioProfessores", "Todos os Professores"))

