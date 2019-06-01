from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from graph import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import numpy as np

#Наши данные
x = pd.read_excel('Temp.xlsx')

#Исходный график


#Создаем приложение
app = QtWidgets.QApplication(sys.argv)

#Формы
mainWindow = QtWidgets.QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
def addmpl():
    canvas = FigureCanvas(fig)
    ui.mplWidget.addWidget(canvas)
    canvas.draw()

#Логика нашего приложения
ui.pushButton_2.clicked.connect(lambda: Result())
ui.pushButton.clicked.connect(lambda: Result2())
ui.pushButton_3.clicked.connect(lambda: Result3())
ui.pushButton_4.clicked.connect(newgraphic())



def Result():
    r1 = x['Temp'].count()
    ui.lineEdit.setText(str(r1))

def Result2():
    r2 = x['Temp'].mean()
    ui.lineEdit.setText(str(r2))

def Result3():
    r3 = x['Temp'].median()
    ui.lineEdit.setText(str(r3))

def graphic():
    sst = x
    n = len(sst)
    dt = 0.25
    fig = plt.figure(figsize=(20, 10))
    time = np.arange(n)  # Дни 365
    xlim = [-20, 385]  # Масштаб
    plt.plot(time, sst)
    xrange = plt.xlim(xlim)
    plt.title('Исходный график 2017-2018', fontsize=30)
    plt.show()


#Выход из приложения
sys.exit(app.exec_())