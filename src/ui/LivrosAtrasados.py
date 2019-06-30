# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LivrosAtrasados.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LivrosAtrasados(object):
    def setupUi(self, LivrosAtrasados):
        LivrosAtrasados.setObjectName("LivrosAtrasados")
        LivrosAtrasados.resize(525, 388)
        self.BigText = QtWidgets.QLabel(LivrosAtrasados)
        self.BigText.setGeometry(QtCore.QRect(20, 10, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BigText.setFont(font)
        self.BigText.setObjectName("BigText")
        self.tabelaRelatorio = QtWidgets.QTableWidget(LivrosAtrasados)
        self.tabelaRelatorio.setGeometry(QtCore.QRect(20, 60, 481, 271))
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

        self.retranslateUi(LivrosAtrasados)
        QtCore.QMetaObject.connectSlotsByName(LivrosAtrasados)

    def retranslateUi(self, LivrosAtrasados):
        _translate = QtCore.QCoreApplication.translate
        LivrosAtrasados.setWindowTitle(_translate("LivrosAtrasados", "Livros Atrasados"))
        self.BigText.setText(_translate("LivrosAtrasados", "Livros Atrasados"))
        item = self.tabelaRelatorio.horizontalHeaderItem(0)
        item.setText(_translate("LivrosAtrasados", "Código"))
        item = self.tabelaRelatorio.horizontalHeaderItem(1)
        item.setText(_translate("LivrosAtrasados", "Título"))
        item = self.tabelaRelatorio.horizontalHeaderItem(2)
        item.setText(_translate("LivrosAtrasados", "Ano"))

