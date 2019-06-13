# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 310)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.principalUI = QtWidgets.QWidget(MainWindow)
        self.principalUI.setObjectName("principalUI")
        self.welcomeText = QtWidgets.QLabel(self.principalUI)
        self.welcomeText.setEnabled(True)
        self.welcomeText.setGeometry(QtCore.QRect(40, 30, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.welcomeText.setFont(font)
        self.welcomeText.setTextFormat(QtCore.Qt.AutoText)
        self.welcomeText.setObjectName("welcomeText")
        self.startTable = QtWidgets.QTableWidget(self.principalUI)
        self.startTable.setEnabled(True)
        self.startTable.setGeometry(QtCore.QRect(40, 60, 281, 91))
        self.startTable.setMaximumSize(QtCore.QSize(500, 16777215))
        self.startTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.startTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.startTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.startTable.setAlternatingRowColors(True)
        self.startTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.startTable.setGridStyle(QtCore.Qt.SolidLine)
        self.startTable.setWordWrap(False)
        self.startTable.setCornerButtonEnabled(True)
        self.startTable.setColumnCount(2)
        self.startTable.setObjectName("startTable")
        self.startTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
        self.startTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
        self.startTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.startTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.startTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.startTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.startTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.startTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.startTable.setItem(1, 1, item)
        self.startTable.horizontalHeader().setVisible(True)
        self.startTable.horizontalHeader().setCascadingSectionResizes(False)
        self.startTable.horizontalHeader().setDefaultSectionSize(120)
        self.startTable.horizontalHeader().setHighlightSections(True)
        self.startTable.horizontalHeader().setMinimumSectionSize(15)
        self.startTable.horizontalHeader().setSortIndicatorShown(False)
        self.startTable.horizontalHeader().setStretchLastSection(False)
        self.startTable.verticalHeader().setVisible(True)
        self.startTable.verticalHeader().setCascadingSectionResizes(False)
        self.startTable.verticalHeader().setSortIndicatorShown(False)
        self.startTable.verticalHeader().setStretchLastSection(True)
        self.buttonEmprestimo = QtWidgets.QPushButton(self.principalUI)
        self.buttonEmprestimo.setGeometry(QtCore.QRect(292, 200, 131, 32))
        self.buttonEmprestimo.setObjectName("buttonEmprestimo")
        MainWindow.setCentralWidget(self.principalUI)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 450, 22))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName("menuBar")
        self.menuArquivo = QtWidgets.QMenu(self.menuBar)
        self.menuArquivo.setToolTipsVisible(False)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuUsuarios = QtWidgets.QMenu(self.menuBar)
        self.menuUsuarios.setObjectName("menuUsuarios")
        self.menuLivros = QtWidgets.QMenu(self.menuBar)
        self.menuLivros.setObjectName("menuLivros")
        self.menuRelatorios = QtWidgets.QMenu(self.menuBar)
        self.menuRelatorios.setObjectName("menuRelatorios")
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalvar_Dados = QtWidgets.QAction(MainWindow)
        self.actionSalvar_Dados.setObjectName("actionSalvar_Dados")
        self.actionCarregar_Dados = QtWidgets.QAction(MainWindow)
        self.actionCarregar_Dados.setObjectName("actionCarregar_Dados")
        self.actionPreferencias = QtWidgets.QAction(MainWindow)
        self.actionPreferencias.setObjectName("actionPreferencias")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionNovo_Aluno = QtWidgets.QAction(MainWindow)
        self.actionNovo_Aluno.setObjectName("actionNovo_Aluno")
        self.actionNovo_Professor = QtWidgets.QAction(MainWindow)
        self.actionNovo_Professor.setObjectName("actionNovo_Professor")
        self.actionVer_Usuarios = QtWidgets.QAction(MainWindow)
        self.actionVer_Usuarios.setObjectName("actionVer_Usuarios")
        self.actionNovo_Livro = QtWidgets.QAction(MainWindow)
        self.actionNovo_Livro.setObjectName("actionNovo_Livro")
        self.actionVer_Livros = QtWidgets.QAction(MainWindow)
        self.actionVer_Livros.setObjectName("actionVer_Livros")
        self.actionTodos_os_usuarios = QtWidgets.QAction(MainWindow)
        self.actionTodos_os_usuarios.setObjectName("actionTodos_os_usuarios")
        self.actionTodos_os_alunos = QtWidgets.QAction(MainWindow)
        self.actionTodos_os_alunos.setObjectName("actionTodos_os_alunos")
        self.actionTodos_os_professores = QtWidgets.QAction(MainWindow)
        self.actionTodos_os_professores.setObjectName("actionTodos_os_professores")
        self.actionHistorico_de_usuario = QtWidgets.QAction(MainWindow)
        self.actionHistorico_de_usuario.setObjectName("actionHistorico_de_usuario")
        self.actionEmprestimos_de_um_usuario = QtWidgets.QAction(MainWindow)
        self.actionEmprestimos_de_um_usuario.setObjectName("actionEmprestimos_de_um_usuario")
        self.actionTodos_os_livros = QtWidgets.QAction(MainWindow)
        self.actionTodos_os_livros.setObjectName("actionTodos_os_livros")
        self.actionLivros_disponiveis = QtWidgets.QAction(MainWindow)
        self.actionLivros_disponiveis.setObjectName("actionLivros_disponiveis")
        self.actionLivros_emprestados = QtWidgets.QAction(MainWindow)
        self.actionLivros_emprestados.setObjectName("actionLivros_emprestados")
        self.actionAtrasos = QtWidgets.QAction(MainWindow)
        self.actionAtrasos.setObjectName("actionAtrasos")
        self.actionUsuarios_com_atrasos = QtWidgets.QAction(MainWindow)
        self.actionUsuarios_com_atrasos.setObjectName("actionUsuarios_com_atrasos")
        self.menuArquivo.addAction(self.actionSalvar_Dados)
        self.menuArquivo.addAction(self.actionCarregar_Dados)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionPreferencias)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionSair)
        self.menuUsuarios.addAction(self.actionNovo_Aluno)
        self.menuUsuarios.addAction(self.actionNovo_Professor)
        self.menuUsuarios.addSeparator()
        self.menuUsuarios.addAction(self.actionVer_Usuarios)
        self.menuLivros.addAction(self.actionNovo_Livro)
        self.menuLivros.addAction(self.actionVer_Livros)
        self.menuRelatorios.addAction(self.actionTodos_os_usuarios)
        self.menuRelatorios.addAction(self.actionTodos_os_alunos)
        self.menuRelatorios.addAction(self.actionTodos_os_professores)
        self.menuRelatorios.addAction(self.actionTodos_os_livros)
        self.menuRelatorios.addSeparator()
        self.menuRelatorios.addAction(self.actionLivros_disponiveis)
        self.menuRelatorios.addAction(self.actionLivros_emprestados)
        self.menuRelatorios.addSeparator()
        self.menuRelatorios.addAction(self.actionHistorico_de_usuario)
        self.menuRelatorios.addAction(self.actionEmprestimos_de_um_usuario)
        self.menuRelatorios.addSeparator()
        self.menuRelatorios.addAction(self.actionUsuarios_com_atrasos)
        self.menuRelatorios.addAction(self.actionAtrasos)
        self.menuBar.addAction(self.menuArquivo.menuAction())
        self.menuBar.addAction(self.menuUsuarios.menuAction())
        self.menuBar.addAction(self.menuLivros.menuAction())
        self.menuBar.addAction(self.menuRelatorios.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema da Biblioteca"))
        self.welcomeText.setText(_translate("MainWindow", "Bem Vindo, Bibliotecário!!"))
        self.startTable.setSortingEnabled(False)
        item = self.startTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Resumo"))
        item = self.startTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Qtd"))
        __sortingEnabled = self.startTable.isSortingEnabled()
        self.startTable.setSortingEnabled(False)
        item = self.startTable.item(0, 0)
        item.setText(_translate("MainWindow", "Livros Emprestados"))
        item = self.startTable.item(1, 0)
        item.setText(_translate("MainWindow", "Livros em atraso"))
        self.startTable.setSortingEnabled(__sortingEnabled)
        self.buttonEmprestimo.setText(_translate("MainWindow", "Novo empréstimo"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuUsuarios.setTitle(_translate("MainWindow", "Usuários"))
        self.menuLivros.setTitle(_translate("MainWindow", "Livros"))
        self.menuRelatorios.setTitle(_translate("MainWindow", "Relatórios"))
        self.actionSalvar_Dados.setText(_translate("MainWindow", "Salvar Dados"))
        self.actionCarregar_Dados.setText(_translate("MainWindow", "Carregar Dados"))
        self.actionPreferencias.setText(_translate("MainWindow", "Preferencias"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionNovo_Aluno.setText(_translate("MainWindow", "Novo Aluno"))
        self.actionNovo_Professor.setText(_translate("MainWindow", "Novo Professor"))
        self.actionVer_Usuarios.setText(_translate("MainWindow", "Ver Usuarios"))
        self.actionNovo_Livro.setText(_translate("MainWindow", "Novo Livro"))
        self.actionVer_Livros.setText(_translate("MainWindow", "Ver Livros"))
        self.actionTodos_os_usuarios.setText(_translate("MainWindow", "Todos os Usuarios"))
        self.actionTodos_os_alunos.setText(_translate("MainWindow", "Todos os Alunos"))
        self.actionTodos_os_professores.setText(_translate("MainWindow", "Todos os Professores"))
        self.actionHistorico_de_usuario.setText(_translate("MainWindow", "Historico de usuario"))
        self.actionEmprestimos_de_um_usuario.setText(_translate("MainWindow", "Emprestimos de um usuario"))
        self.actionTodos_os_livros.setText(_translate("MainWindow", "Todos os livros"))
        self.actionLivros_disponiveis.setText(_translate("MainWindow", "Livros disponiveis"))
        self.actionLivros_emprestados.setText(_translate("MainWindow", "Livros emprestados"))
        self.actionAtrasos.setText(_translate("MainWindow", "Atrasos"))
        self.actionUsuarios_com_atrasos.setText(_translate("MainWindow", "Usuarios com atrasos"))