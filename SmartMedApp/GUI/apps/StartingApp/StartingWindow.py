# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class StartingWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 463, 21))
        self.label.setObjectName("label")
        self.pushButtonDone = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDone.setGeometry(QtCore.QRect(450, 420, 121, 32))
        self.pushButtonDone.setObjectName("pushButtonDone")
        self.pushButtonStat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStat.setGeometry(QtCore.QRect(90, 90, 401, 32))
        self.pushButtonStat.setObjectName("pushButtonStat")
        self.pushButtonBioeq = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBioeq.setGeometry(QtCore.QRect(90, 200, 401, 32))
        self.pushButtonBioeq.setObjectName("pushButtonBioeq")
        self.pushButtonPred = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPred.setGeometry(QtCore.QRect(90, 310, 401, 32))
        self.pushButtonPred.setObjectName("pushButtonPred")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 360, 381, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 250, 381, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 140, 381, 41))
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.pushButtonDone.raise_()
        self.pushButtonBioeq.raise_()
        self.pushButtonPred.raise_()
        self.pushButtonStat.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Выберите метод исследования данных</span></p><p><span style=\" font-size:18pt;\"><br/></span></p></body></html>"))
        self.pushButtonDone.setText(_translate("MainWindow", "Завершить"))
        self.pushButtonStat.setText(_translate("MainWindow", "Статистический анализ"))
        self.pushButtonBioeq.setText(_translate("MainWindow", "Биоэквивалентность"))   
        self.pushButtonPred.setText(_translate("MainWindow", "Предсказательные модели"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Построение  статистических и предсказательных моделей </span></p><p align=\"center\"><span style=\" font-size:11pt;\">по исследуемым данным: регрессионные модели, ROC-анализ</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Исследование идентичности свойств </span></p><p align=\"center\"><span style=\" font-size:11pt;\">биодоступности у исходного препарата и дженерика</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Получение обобщенной</span></p><p align=\"center\"><span style=\" font-size:11pt;\">информации о данных, Визуальный анализ</span></p><p align=\"center\"><br/></p></body></html>"))
