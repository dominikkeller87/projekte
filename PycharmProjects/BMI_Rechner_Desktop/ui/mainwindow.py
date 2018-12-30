# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 707)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.height = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.height.setMinimum(0.01)
        self.height.setMaximum(2.5)
        self.height.setSingleStep(0.01)
        self.height.setObjectName("height")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.height)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.weight = QtWidgets.QSpinBox(self.centralWidget)
        self.weight.setPrefix("")
        self.weight.setMinimum(1)
        self.weight.setMaximum(999)
        self.weight.setObjectName("weight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.weight)
        self.button = QtWidgets.QPushButton(self.centralWidget)
        self.button.setObjectName("button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.button)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.bmi_value = QtWidgets.QLabel(self.centralWidget)
        self.bmi_value.setObjectName("bmi_value")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bmi_value)
        self.warning = QtWidgets.QLabel(self.centralWidget)
        self.warning.setObjectName("warning")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.warning)
        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 439, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BMI Rechner"))
        self.label.setText(_translate("MainWindow", "K&ouml;rpergr&ouml;&szlig;e in Meter:"))
        self.height.setPrefix(_translate("MainWindow", " "))
        self.height.setSuffix(_translate("MainWindow", " m"))
        self.label_2.setText(_translate("MainWindow", "Gewicht in KG:"))
        self.weight.setSuffix(_translate("MainWindow", " kg"))
        self.button.setText(_translate("MainWindow", "BMI Berechnen"))
        self.label_3.setText(_translate("MainWindow", "Dein BMI ist:"))
        self.bmi_value.setText(_translate("MainWindow", "20"))
        self.warning.setText(_translate("MainWindow", "TextLabel"))

