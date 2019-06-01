# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from graph2 import *
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

x = pd.read_excel('Temp.xlsx')

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(lambda: self.Result())
        self.ui.pushButton.clicked.connect(lambda: self.Result2())
        self.ui.pushButton_3.clicked.connect(lambda: self.Result3())
        self.ui.pushButton_4.clicked.connect(lambda: self.Result4())
        self.ui.pushButton_8.clicked.connect(lambda: self.Result5())

    def Result(self):
        r1 = x['Temp'].count()
        self.ui.lineEdit.setText(str(r1))

    def Result2(self):
        r2 = x['Temp'].mean()
        self.ui.lineEdit.setText(str(r2))

    def Result3(self):
        r3 = x['Temp'].median()
        self.ui.lineEdit.setText(str(r3))

    def Result4(self):
        fs = 500
        f = random.randint(1, 100)
        ts = 1 / fs
        length_of_signal = 100
        t = np.linspace(0, 1, length_of_signal)
        cosinus_signal = np.cos(2 * np.pi * f * t)
        sinus_signal = np.sin(2 * np.pi * f * t)
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(t, cosinus_signal)
        self.ui.MplWidget.canvas.axes.plot(t, sinus_signal)
        self.ui.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
        self.ui.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.ui.MplWidget.canvas.draw()

    def Result5(self):
        sst = x
        n = len(sst)
        dt = 0.25
        fig = plt.figure(figsize=(20, 10))
        time = np.arange(n)  # Дни 365
        xlim = [-20, 385]  # Масштаб
        plt.plot(time, sst)
        xrange = plt.xlim(xlim)
        self.ui.MplWidget.canvas.axes.plot(time, sst)
        self.ui.MplWidget.canvas.axes.set_title('Исходный график')
        self.ui.MplWidget.canvas.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())