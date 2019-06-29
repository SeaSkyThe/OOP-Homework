# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LivrosDisponiveis.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LivrosDisponiveis(object):
    def setupUi(self, LivrosDisponiveis):
        LivrosDisponiveis.setObjectName("LivrosDisponiveis")
        LivrosDisponiveis.resize(539, 384)
        self.tabelaRelatorio = QtWidgets.QTableWidget(LivrosDisponiveis)
        self.tabelaRelatorio.setGeometry(QtCore.QRect(30, 70, 481, 271))
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
        self.BigText = QtWidgets.QLabel(LivrosDisponiveis)
        self.BigText.setGeometry(QtCore.QRect(30, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BigText.setFont(font)
        self.BigText.setObjectName("BigText")

        self.retranslateUi(LivrosDisponiveis)
        QtCore.QMetaObject.connectSlotsByName(LivrosDisponiveis)

    def retranslateUi(self, LivrosDisponiveis):
        _translate = QtCore.QCoreApplication.translate
        LivrosDisponiveis.setWindowTitle(_translate("LivrosDisponiveis", "Livros Disponiveis"))
        item = self.tabelaRelatorio.horizontalHeaderItem(0)
        item.setText(_translate("LivrosDisponiveis", "Código"))
        item = self.tabelaRelatorio.horizontalHeaderItem(1)
        item.setText(_translate("LivrosDisponiveis", "Título"))
        item = self.tabelaRelatorio.horizontalHeaderItem(2)
        item.setText(_translate("LivrosDisponiveis", "Ano"))
        self.BigText.setText(_translate("LivrosDisponiveis", "Livros Disponiveis"))

