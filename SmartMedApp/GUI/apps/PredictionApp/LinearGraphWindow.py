# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LinearGraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class LinearGraphWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 511, 41))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 120, 418, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxQuality = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxQuality.setObjectName("checkBoxQuality")
        self.verticalLayout.addWidget(self.checkBoxQuality)
        self.checkBoxSignif = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxSignif.setObjectName("checkBoxSignif")
        self.verticalLayout.addWidget(self.checkBoxSignif)
        self.checkBoxEq = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxEq.setObjectName("checkBoxEq")
        self.verticalLayout.addWidget(self.checkBoxEq)
        self.checkBoxResid = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxResid.setObjectName("checkBoxResid")
        self.verticalLayout.addWidget(self.checkBoxResid)
        self.checkBoxDistribResid = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxDistribResid.setObjectName("checkBoxDistribResid")
        self.verticalLayout.addWidget(self.checkBoxDistribResid)
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(330, 420, 113, 32))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.pushButtonDone = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDone.setGeometry(QtCore.QRect(460, 420, 113, 32))
        self.pushButtonDone.setObjectName("pushButtonDone")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt;\">Выберите таблицы и графики</span></p></body></html>"))
        self.checkBoxQuality.setText(_translate("MainWindow", "  Таблица с критериями качества построенной модели"))
        self.checkBoxSignif.setText(_translate("MainWindow", "  Таблица с критериями значимости для каждой \n "
" независимой переменной"))
        self.checkBoxEq.setText(_translate("MainWindow", "  Полученное уравнение регрессии с возможностью  \n  ввода собственных переменных"))
        self.checkBoxResid.setText(_translate("MainWindow", "  Таблица с анализами остатков"))
        self.checkBoxDistribResid.setText(_translate("MainWindow", "  Графики распределения остатков "))
        self.pushButtonBack.setText(_translate("MainWindow", "Назад"))
        self.pushButtonDone.setText(_translate("MainWindow", "Завершить"))
