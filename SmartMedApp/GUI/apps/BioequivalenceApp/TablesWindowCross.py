# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TablesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TablesWindowCross(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 20, 461, 71))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 130, 449, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxCriteria = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxCriteria.setObjectName("checkBoxCriteria")
        self.verticalLayout.addWidget(self.checkBoxCriteria)
        self.checkBoxFeatures = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxFeatures.setObjectName("checkBoxFeatures")
        self.verticalLayout.addWidget(self.checkBoxFeatures)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.pushButtonNext = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonNext.setGeometry(QtCore.QRect(460, 420, 113, 32))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonBack = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(330, 420, 113, 32))
        self.pushButtonBack.setObjectName("pushButtonBack")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:13pt;\">Выберите нужные таблицы</span></p></body></html>"))
        self.checkBoxCriteria.setText(_translate("MainWindow", "  Средние площади под графиком по каждому препарату "))
        self.checkBoxFeatures.setText(_translate("MainWindow", "  Результаты двухфакторного дисперсионного анализа"))
        self.checkBox.setText(_translate("MainWindow", "  Результаты оценки биоэквивалентности"))
        self.pushButtonNext.setText(_translate("MainWindow", "Вперед"))
        self.pushButtonBack.setText(_translate("MainWindow", "Назад"))
