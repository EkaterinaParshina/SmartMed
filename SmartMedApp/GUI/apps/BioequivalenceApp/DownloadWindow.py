# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_down.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class DownloadWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 500, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 561, 250))
        self.label_2.setObjectName("label_2")
        self.pushButtonDownload = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDownload.setGeometry(QtCore.QRect(85, 330, 113, 32))
        self.pushButtonDownload.setObjectName("pushButtonDownload")
        self.pushButtonDownload1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDownload1.setGeometry(QtCore.QRect(85, 385, 113, 32))
        self.pushButtonDownload1.setObjectName("pushButtonDownload1")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 305, 480, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 360, 480, 31))
        self.label_4.setObjectName("label_4")
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(330, 420, 113, 32))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.pushButton_ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_.setGeometry(QtCore.QRect(460, 420, 113, 32))
        self.pushButton_.setObjectName("pushButton_")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:17pt;\">Загрузка данных</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Данные должны быть загружены в формате “.xlsx”, “.xs” или “.csv”. </span></p><p><span style=\" font-size:9pt;\">Необходима загрузка двух файлов. Первый файл должен содержать данные </span></p><p><span style=\" font-size:9pt;\">с концентрацией тестового препарата в крови пациентов. </span></p><p><span style=\" font-size:9pt;\">Второй файл должен содержать данные с концентрацией референсного</span></p><p><span style=\" font-size:9pt;\">препарата в крови пациентов. </span></p><p><span style=\" font-size:9pt;\">Необходимо, чтобы в первой строке каждого файла был указан момент</span></p><p><span style=\" font-size:9pt;\"> времени (в часах),в который была зафиксирована концентрация. </span></p><p><span style=\" font-size:9pt;\">В первом столбце каждого файла нужно указать порядковый номер пациента. </span></p></body></html>"))
        self.pushButtonDownload.setText(_translate("MainWindow", "Загрузить"))
        self.pushButtonDownload1.setText(_translate("MainWindow", "Загрузить"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Данные по тестовому препарату</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Данные по референсному препарату</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.pushButtonBack.setText(_translate("MainWindow", "Назад"))
        self.pushButton_.setText(_translate("MainWindow", "Вперед"))
