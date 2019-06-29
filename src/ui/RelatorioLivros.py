# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RelatorioLivros.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RelatorioLivros(object):
    def setupUi(self, RelatorioLivros):
        RelatorioLivros.setObjectName("RelatorioLivros")
        RelatorioLivros.resize(568, 402)
        self.BigText = QtWidgets.QLabel(RelatorioLivros)
        self.BigText.setGeometry(QtCore.QRect(40, 10, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BigText.setFont(font)
        self.BigText.setObjectName("BigText")
        self.tabelaRelatorio = QtWidgets.QTableWidget(RelatorioLivros)
        self.tabelaRelatorio.setGeometry(QtCore.QRect(40, 70, 501, 291))
        self.tabelaRelatorio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabelaRelatorio.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabelaRelatorio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabelaRelatorio.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabelaRelatorio.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabelaRelatorio.setDragEnabled(False)
        self.tabelaRelatorio.setObjectName("tabelaRelatorio")
        self.tabelaRelatorio.setColumnCount(5)
        self.tabelaRelatorio.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(4, item)
        self.tabelaRelatorio.horizontalHeader().setSortIndicatorShown(False)
        self.tabelaRelatorio.horizontalHeader().setStretchLastSection(False)

        self.retranslateUi(RelatorioLivros)
        QtCore.QMetaObject.connectSlotsByName(RelatorioLivros)

    def retranslateUi(self, RelatorioLivros):
        _translate = QtCore.QCoreApplication.translate
        RelatorioLivros.setWindowTitle(_translate("RelatorioLivros", "Dialog"))
        self.BigText.setText(_translate("RelatorioLivros", "Todos os Livros"))
        item = self.tabelaRelatorio.horizontalHeaderItem(0)
        item.setText(_translate("RelatorioLivros", "Código"))
        item = self.tabelaRelatorio.horizontalHeaderItem(1)
        item.setText(_translate("RelatorioLivros", "Título"))
        item = self.tabelaRelatorio.horizontalHeaderItem(2)
        item.setText(_translate("RelatorioLivros", "Ano"))
        item = self.tabelaRelatorio.horizontalHeaderItem(3)
        item.setText(_translate("RelatorioLivros", "Emprestado"))
        item = self.tabelaRelatorio.horizontalHeaderItem(4)
        item.setText(_translate("RelatorioLivros", "Atrasado"))
