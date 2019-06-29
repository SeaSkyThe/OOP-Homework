# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LivrosEmprestados.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LivrosEmprestados(object):
    def setupUi(self, LivrosEmprestados):
        LivrosEmprestados.setObjectName("LivrosEmprestados")
        LivrosEmprestados.resize(539, 385)
        self.tabelaRelatorio = QtWidgets.QTableWidget(LivrosEmprestados)
        self.tabelaRelatorio.setGeometry(QtCore.QRect(30, 90, 481, 271))
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
        self.BigText = QtWidgets.QLabel(LivrosEmprestados)
        self.BigText.setGeometry(QtCore.QRect(30, 20, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BigText.setFont(font)
        self.BigText.setObjectName("BigText")

        self.retranslateUi(LivrosEmprestados)
        QtCore.QMetaObject.connectSlotsByName(LivrosEmprestados)

    def retranslateUi(self, LivrosEmprestados):
        _translate = QtCore.QCoreApplication.translate
        LivrosEmprestados.setWindowTitle(_translate("LivrosEmprestados", "Livros Emprestados"))
        item = self.tabelaRelatorio.horizontalHeaderItem(0)
        item.setText(_translate("LivrosEmprestados", "Código"))
        item = self.tabelaRelatorio.horizontalHeaderItem(1)
        item.setText(_translate("LivrosEmprestados", "Título"))
        item = self.tabelaRelatorio.horizontalHeaderItem(2)
        item.setText(_translate("LivrosEmprestados", "Ano"))
        self.BigText.setText(_translate("LivrosEmprestados", "Livros Emprestados"))

