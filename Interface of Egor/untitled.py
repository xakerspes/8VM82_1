# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Egor Ivanov\Desktop\test\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineediturl = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineediturl.setObjectName("lineediturl")
        self.verticalLayout.addWidget(self.lineediturl)
        self.downloadpush = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.downloadpush.setObjectName("downloadpush")
        self.verticalLayout.addWidget(self.downloadpush)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.pokazatdatu = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pokazatdatu.setObjectName("pokazatdatu")
        self.verticalLayout.addWidget(self.pokazatdatu)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.dataot = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.dataot.setObjectName("dataot")
        self.verticalLayout.addWidget(self.dataot)
        self.datado = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.datado.setObjectName("datado")
        self.verticalLayout.addWidget(self.datado)
        self.periodpush = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.periodpush.setObjectName("periodpush")
        self.verticalLayout.addWidget(self.periodpush)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.countpush = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.countpush.setObjectName("countpush")
        self.verticalLayout.addWidget(self.countpush)
        self.meanpush = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.meanpush.setObjectName("meanpush")
        self.verticalLayout.addWidget(self.meanpush)
        self.medianpush = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.medianpush.setObjectName("medianpush")
        self.verticalLayout.addWidget(self.medianpush)
        self.lineEditstat = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditstat.setObjectName("lineEditstat")
        self.verticalLayout.addWidget(self.lineEditstat)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(400, 10, 351, 621))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.maingraphpush = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.maingraphpush.setObjectName("maingraphpush")
        self.verticalLayout_2.addWidget(self.maingraphpush)
        self.furiepush = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.furiepush.setObjectName("furiepush")
        self.verticalLayout_2.addWidget(self.furiepush)
        self.mhatpush = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.mhatpush.setObjectName("mhatpush")
        self.verticalLayout_2.addWidget(self.mhatpush)
        self.morletpush = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.morletpush.setObjectName("morletpush")
        self.verticalLayout_2.addWidget(self.morletpush)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Научная работа"))
        self.label.setText(_translate("MainWindow", "Шаг 1. Загрузка данных "))
        self.lineediturl.setPlaceholderText(_translate("MainWindow", "Введите сыллку на данные"))
        self.downloadpush.setText(_translate("MainWindow", "Загрузка данных"))
        self.label_2.setText(_translate("MainWindow", "Шаг 2. Выбор периода"))
        self.label_3.setText(_translate("MainWindow", "Выбор периода"))
        self.dataot.setPlaceholderText(_translate("MainWindow", "Введите дату от / в таком формате (год.месяц.дата)"))
        self.datado.setPlaceholderText(_translate("MainWindow", "Введите дату от / в таком формате (год.месяц.дата)"))
        self.periodpush.setText(_translate("MainWindow", "Выбор указаного периода"))
        self.label_4.setText(_translate("MainWindow", "Шаг 3. Основная статистика"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Импульс (Север-Юг)"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Амплитуда (Север-Юг)"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Импульс (Запад-Восток)"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Амплитуда (Запад-Восток)"))
        self.countpush.setText(_translate("MainWindow", "Количество данных"))
        self.meanpush.setText(_translate("MainWindow", "Среднее значение данных"))
        self.medianpush.setText(_translate("MainWindow", "Медиана данных"))
        self.label_5.setText(_translate("MainWindow", "Шаг 4. Визуализация данных"))
        self.maingraphpush.setText(_translate("MainWindow", "Исходный график"))
        self.furiepush.setText(_translate("MainWindow", "Преобразование Фурье"))
        self.mhatpush.setText(_translate("MainWindow", "Вейвлет преобразование MHAT"))
        self.morletpush.setText(_translate("MainWindow", "Вейвлет преобразование Morlet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

