# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UsuariosAtraso.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UsuariosAtraso(object):
    def setupUi(self, UsuariosAtraso):
        UsuariosAtraso.setObjectName("UsuariosAtraso")
        UsuariosAtraso.resize(552, 390)
        self.BigText = QtWidgets.QLabel(UsuariosAtraso)
        self.BigText.setGeometry(QtCore.QRect(20, 0, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.BigText.setFont(font)
        self.BigText.setObjectName("BigText")
        self.tabelaRelatorio = QtWidgets.QTableWidget(UsuariosAtraso)
        self.tabelaRelatorio.setGeometry(QtCore.QRect(40, 60, 481, 291))
        self.tabelaRelatorio.setMouseTracking(False)
        self.tabelaRelatorio.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabelaRelatorio.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tabelaRelatorio.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tabelaRelatorio.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabelaRelatorio.setDragEnabled(False)
        self.tabelaRelatorio.setAlternatingRowColors(True)
        self.tabelaRelatorio.setObjectName("tabelaRelatorio")
        self.tabelaRelatorio.setColumnCount(2)
        self.tabelaRelatorio.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelaRelatorio.setHorizontalHeaderItem(1, item)
        self.tabelaRelatorio.horizontalHeader().setSortIndicatorShown(False)
        self.tabelaRelatorio.horizontalHeader().setStretchLastSection(False)

        self.retranslateUi(UsuariosAtraso)
        QtCore.QMetaObject.connectSlotsByName(UsuariosAtraso)

    def retranslateUi(self, UsuariosAtraso):
        _translate = QtCore.QCoreApplication.translate
        UsuariosAtraso.setWindowTitle(_translate("UsuariosAtraso", "Usuários com Atraso"))
        self.BigText.setText(_translate("UsuariosAtraso", "Usuários com atraso"))
        item = self.tabelaRelatorio.horizontalHeaderItem(0)
        item.setText(_translate("UsuariosAtraso", "Cod de Usuário"))
        item = self.tabelaRelatorio.horizontalHeaderItem(1)
        item.setText(_translate("UsuariosAtraso", "Nome"))

