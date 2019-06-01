# -*- coding: utf-8 -*-
import sys
from graph2 import *
import pandas as pd
import numpy as np
import random
import scipy.fftpack
import scipy as sp
from scipy import signal
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)



#x = pd.read_excel('Temp.xlsx')
x = pd.read_excel('data.xlsx', encoding='windows-1252')
x.set_index('Time', inplace=True)

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(lambda: self.Result())
        self.ui.pushButton.clicked.connect(lambda: self.Result2())
        self.ui.pushButton_3.clicked.connect(lambda: self.Result3())
        self.ui.pushButton_4.clicked.connect(lambda: self.Result5())
        self.ui.pushButton_8.clicked.connect(lambda: self.Result4())
        self.ui.pushButton_5.clicked.connect(lambda: self.Result6())

    def Result(self):
        #Количество
        r1 = x['Temp'].count()
        self.ui.lineEdit.setText(str(r1))

    def Result2(self):
        #Среднее значение
        #xs = sum(xs)/len(xs)
        r2 = x['Temp'].mean()
        self.ui.lineEdit.setText(str(r2))

    def Result3(self):
        #Медиана
        #n = len(xs)
        #mid = n // 2
        #if n % 2 == 1:
            #return (sorted(xs)[mid])
        #else:
            #mean(sorted(xs)[mid-1:][:2])
        r3 = x['Temp'].median()
        self.ui.lineEdit.setText(str(r3))

    def Result4(self):
        #Исходный график
        sst = x['Temp']
        n = len(sst)
        time = np.arange(n)  # Дни 365
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(time, sst)
        self.ui.MplWidget.canvas.axes.set_title('Исходный график')
        self.ui.MplWidget.canvas.draw()

    def Result5(self):
        #Преобразование Фурье
        data = x['2017-12-31 18:31:00+00':'2018-01-31 18:29:00+00']
        data_per = data['Temp']
        temp_fft = sp.fftpack.fft(data_per)
        temp_psd = np.abs(temp_fft) ** 2
        fftfreq = sp.fftpack.fftfreq(len(temp_psd), 1)
        i = fftfreq > 0
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(fftfreq[i], 10 * np.log10(temp_psd[i]))
        self.ui.MplWidget.canvas.axes.set_title('Преобразование Фурье')
        self.ui.MplWidget.canvas.draw()

    def Result6(self):
        widths = np.arange(1, 900)
        cwtmatr = signal.cwt(x['Temp'], signal.ricker, widths)
        self.ui.MplWidget.canvas.axes()
        self.ui.MplWidget.canvas.axes.plot(cwtmatr, extent=[1, 44635, -40, 20], cmap='PRGn', aspect='auto', vmax=abs(cwtmatr).max(),vmin=-abs(cwtmatr).max())
        self.ui.MplWidget.canvas.draw()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())