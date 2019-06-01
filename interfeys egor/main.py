# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from untitled import *
from collections import Counter
import scipy as sp
from scipy import stats
import pandas as pd
import numpy as np

x = pd.read_excel('Temp.xlsx')

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(lambda: self.Result())
        self.ui.pushButton.clicked.connect(lambda: self.Result2())
        self.ui.pushButton_3.clicked.connect(lambda: self.Result3())

    def Result(self):
        r1 = x['Temp'].count()
        self.ui.lineEdit.setText(str(r1))

    def Result2(self):
        r2 = x['Temp'].mean()
        self.ui.lineEdit.setText(str(r2))

    def Result3(self):
        r3 = x['Temp'].median()
        self.ui.lineEdit.setText(str(r3))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())