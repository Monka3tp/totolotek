# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(373, 212)
        Dialog.setStyleSheet("background-color:lightblue;")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 9, 341, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.obstawiamEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.obstawiamEdit.setStyleSheet("background-color:white")
        self.obstawiamEdit.setObjectName("obstawiamEdit")
        self.gridLayout.addWidget(self.obstawiamEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.losowanieEdit = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.losowanieEdit.setStyleSheet("background-color:white")
        self.losowanieEdit.setObjectName("losowanieEdit")
        self.gridLayout.addWidget(self.losowanieEdit, 2, 1, 1, 1)
        self.generujButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.generujButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.generujButton.setStyleSheet("background-color:white")
        self.generujButton.setObjectName("generujButton")
        self.gridLayout.addWidget(self.generujButton, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.trafieniaButton = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.trafieniaButton.setStyleSheet("background-color:white")
        self.trafieniaButton.setObjectName("trafieniaButton")
        self.gridLayout.addWidget(self.trafieniaButton, 3, 1, 1, 1)
        self.losujButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.losujButton.setMinimumSize(QtCore.QSize(100, 0))
        self.losujButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.losujButton.setStyleSheet("background-color:white")
        self.losujButton.setObjectName("losujButton")
        self.gridLayout.addWidget(self.losujButton, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Trafienia:"))
        self.label_2.setText(_translate("Dialog", "Wynik losowania:"))
        self.generujButton.setText(_translate("Dialog", "Generuj"))
        self.label.setText(_translate("Dialog", "Obstawiam: "))
        self.losujButton.setText(_translate("Dialog", "Losuj"))
