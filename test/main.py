from PyQt5 import QtCore, QtGui, QtWidgets
from untitled import Ui_MainWindow
from datetime import datetime
from scipy import signal
import sys
import re
import urllib.request
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.fftpack


#Инициализация приложения
app = QtWidgets.QApplication(sys.argv)
#Форма
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


# -----------------------------------------------------------------------------------------------------------------
#Логика приложения


# -----------------------------------------------------------------------------------------------------------------


def get_name_of_files():#принимает коренную ссылку
    if (ui.lineediturl.text() == ''):
        url_of_station = "http://mgr.imces.ru/stdpub/mgr-baikal/hsg-irkutsk/"
    else:
        url_of_station = ui.lineediturl.text()
    html  = urllib.request.urlopen(url_of_station)
    page  = html.read()
    pattern = re.compile('"(\w+\.\w+)')
    result = re.findall(pattern ,str(page))
    ui.comboBox_2.clear()
    ui.comboBox_2.addItems(result)
    pass
    
# -----------------------------------------------------------------------------------------------------------------

ui.pushButton.clicked.connect( get_name_of_files )

def Download():
    if (ui.lineediturl.text() == ''):
        url_of_station = "http://mgr.imces.ru/stdpub/mgr-baikal/hsg-irkutsk/"
    else:
        url_of_station = ui.lineediturl.text()
    text_of_file = ui.comboBox_2.currentText()
    url_of_file = "".join((url_of_station, text_of_file))
    page = urllib.request.urlopen(url_of_file)
    content = page.read()
    
    type_file = url_of_file.split('.')
    if type_file[-1] == 'gr1':
        width = 8  # shirina fayla gr1
        numpy_data_polojitelnie = np.frombuffer(content, dtype=np.dtype('B')).reshape(int(len(content) / width), width)
        length_column = int(len(
            content) / width) - 2  # вычитаем -2 так как первые 16 байтов являтся заголовком, каждая строка по 8 байтам и не читаем первые две строки
        numpy_date = np.array(numpy_data_polojitelnie[2:, :4], dtype=np.uint32)

    if type_file[-1] == 'gr2':
        width = 12  # shirina fayla gr2
        numpy_data_polojitelnie = np.frombuffer(content, dtype=np.dtype('B')).reshape(int(len(content) / width), width)
        length_column = int(len(content) / width) - 1  # вычитаем -1 так как первые 12 байтов являтся заголовком
        numpy_date = np.array(numpy_data_polojitelnie[1:, :4], dtype=np.uint32)

    if type_file[-1] == 'mgr':
        width = 13  # shirina fayla mgr
        numpy_data_polojitelnie = np.frombuffer(content, dtype=np.dtype('B')).reshape(int(len(content) / width), width)
        length_column = int(len(content) / width) - 1  # вычитаем -1 так как первые 13 байтов являтся заголовком
        numpy_date_temp = np.array(numpy_data_polojitelnie[1:, :3], dtype=np.uint32)
        numpy_date = []
        b = np.array(numpy_date_temp, dtype='U2')
        for i in range(len(numpy_date_temp)):
            numpy_date.append(b[i, 0] + ':' + b[i, 1] + ':' + b[i, 2])
        array_date_obichniy_format = np.array(numpy_date, dtype='U7')
        # -----------------------------------------------------------------------------------------------------------------
    if width == 8:  # это означает что ширина = 8 то есть фалй gr1
        numpy_H1_amp_count = numpy_data_polojitelnie[2:, 4:6]
        numpy_H1_amplituda = numpy_data_polojitelnie[2:, 6:8]

    if width == 12:  # это означает что ширина = 12 то есть фалй gr2
        numpy_H1_amp_count = numpy_data_polojitelnie[1:, 4:6]
        numpy_H1_amplituda = numpy_data_polojitelnie[1:, 6:8]
        numpy_H2_amp_count = numpy_data_polojitelnie[1:, 8:10]
        numpy_H2_amplituda = numpy_data_polojitelnie[1:, 10:12]

    if width == 13:  # это означает что ширина = 13 то есть фалй mgr
        numpy_H1_amp_count = numpy_data_polojitelnie[1:, 3:5]
        numpy_H2_amp_count = numpy_data_polojitelnie[1:, 5:7]
        numpy_E_amp_count = numpy_data_polojitelnie[1:, 7:9]
        numpy_H1_amplituda = numpy_data_polojitelnie[1:, 9:11]
        numpy_H2_amplituda = numpy_data_polojitelnie[1:, 11:13]

        # -----------------------------------------------------------------------------------------------------------------

    
    def date_v_sekundax(massiv):
        s = np.zeros(length_column, dtype='uint64')
        for i in range(length_column):
            s[i] = massiv[i, 3] * (pow(16, 6)) + massiv[i, 1] * (pow(16, 4)) + massiv[i, 2] * (pow(16, 2)) + massiv[
                i, 0]
        return s

    if width == 8 or width == 12:
        array_date_v_sekundax = date_v_sekundax(numpy_date)
# -----------------------------------------------------------------------------------------------------------------

    def data_obichniy_format(massiv):
        s = np.zeros(length_column, dtype='<U40')  # "<U36"dlina simvolov
        for i in range(len(massiv)):
            s[i] = datetime.fromtimestamp(massiv[i] - 2209032000).strftime("%Y.%m.%d, %I:%M:%S")
        return s

    if width == 8 or width == 12:
        array_date_obichniy_format = data_obichniy_format(array_date_v_sekundax)
# -----------------------------------------------------------------------------------------------------------------

    def func_join_2_column(massiv):
        s = np.zeros(length_column, dtype='uint32')
        for i in range(length_column):
            s[i] = massiv[i, 0] + massiv[i, 1] * 16
        return s
        # -----------------------------------------------------------------------------------------------------------------

    if width == 8:
        array_H1_amp_count = func_join_2_column(numpy_H1_amp_count)
        array_H1_amplituda = func_join_2_column(numpy_H1_amplituda)

        dataset = pd.DataFrame(
            {'Time': array_date_obichniy_format, 'ImpulseNS': array_H1_amp_count, 'AmplitudaNS': array_H1_amplituda})

    if width == 12:
        array_H1_amp_count = func_join_2_column(numpy_H1_amp_count)
        array_H1_amplituda = func_join_2_column(numpy_H1_amplituda)
        array_H2_amp_count = func_join_2_column(numpy_H2_amp_count)
        array_H2_amplituda = func_join_2_column(numpy_H2_amplituda)

        dataset = pd.DataFrame(
            {'Time': array_date_obichniy_format, 'ImpulseNS': array_H1_amp_count, 'AmplitudaNS': array_H1_amplituda,
             'ImpulseWE': array_H2_amp_count,
             'AmplitudaWE': array_H2_amplituda})

    if width == 13:
        array_H1_amp_count = func_join_2_column(numpy_H1_amp_count)
        array_H2_amp_count = func_join_2_column(numpy_H2_amp_count)
        array_E_amp_count = func_join_2_column(numpy_E_amp_count)
        array_H1_amplituda = func_join_2_column(numpy_H1_amplituda)
        array_H2_amplituda = func_join_2_column(numpy_H2_amplituda)

        dataset = pd.DataFrame(
            {'Time': array_date_obichniy_format, 'ImpulseNS': array_H1_amp_count, 'AmplitudaNS': array_H1_amplituda,
             'ImpulseWE': array_H2_amp_count,
             'AmplitudaWE': array_H2_amplituda})

    x = array_date_obichniy_format[0],array_date_obichniy_format[-1]
    ui.pokazatdatu.setText(str(x))

    return dataset
# -----------------------------------------------------------------------------------------------------------------

ui.downloadpush.clicked.connect( Download )
# -----------------------------------------------------------------------------------------------------------------

def period():
    o = ui.dataot.text()
    w = ui.datado.text()
    mask = (Download()['Time'] > o) & (Download()['Time'] <= w)
    periodopr = Download().loc[mask]
    return periodopr
# -----------------------------------------------------------------------------------------------------------------

ui.periodpush.clicked.connect( period )
# -----------------------------------------------------------------------------------------------------------------



def peredacha():
    x = ui.comboBox.currentText()
    if x == "Импульс (Север-Юг)":
        p = period()['ImpulseNS']
    if x == "Амплитуда (Север-Юг)":
        p = period()['AmplitudaNS']
    if x == "Импульс (Запад-Восток)":
        p = period()['ImpulseWE']
    if x == "Амплитуда (Запад-Восток)":
        p = period()['AmplitudaWE']
    return p
# -----------------------------------------------------------------------------------------------------------------

def colichestvo():
    r1 = peredacha().count()
    ui.lineEditstat.setText(str(r1))
ui.countpush.clicked.connect( colichestvo )
# -----------------------------------------------------------------------------------------------------------------

def sredneeznachenie():
    r2 = peredacha().mean()
    ui.lineEditstat.setText(str(r2))
# -----------------------------------------------------------------------------------------------------------------

ui.meanpush.clicked.connect( sredneeznachenie )

# -----------------------------------------------------------------------------------------------------------------

def mediana():
    r3 = peredacha().median()
    ui.lineEditstat.setText(str(r3))
# -----------------------------------------------------------------------------------------------------------------

ui.medianpush.clicked.connect( mediana )

# -----------------------------------------------------------------------------------------------------------------

def maingraph():
    sst = peredacha()
    n = len(sst)
    time = np.arange(n)
    dt = 0.25
    fig = plt.figure(figsize=(20, 10))
    time = np.arange(n)
    xlim = [0, n]
    plt.plot(time, sst)
    xrange = plt.xlim(xlim)
    plt.title('Исходный график', fontsize=30)
    plt.show()

# -----------------------------------------------------------------------------------------------------------------

ui.maingraphpush.clicked.connect( maingraph )

# -----------------------------------------------------------------------------------------------------------------

def furietransform():
    temp_fft = sp.fftpack.fft(peredacha())
    temp_psd = np.abs(temp_fft) ** 2
    fftfreq = sp.fftpack.fftfreq(len(temp_psd), 1)
    i = fftfreq > 0
    fig, ax = plt.subplots(1, 1, figsize=(18, 10))
    ax.plot(fftfreq[i], 10 * np.log10(temp_psd[i]))
    ax.set_xlim(0, 0.5)
    ax.set_xlabel('Частота', fontsize=15)
    ax.set_ylabel('Амплитуда', fontsize=15)
    plt.title('Преобразование Фурье', fontsize=25)
    plt.show()
# -----------------------------------------------------------------------------------------------------------------


ui.furiepush.clicked.connect( furietransform )

# -----------------------------------------------------------------------------------------------------------------

def mhat():
    vj = len(peredacha())
    widths = np.arange(1, 61)
    cwtmatr = signal.cwt(peredacha(), signal.ricker, widths)
    fig = plt.figure(figsize=(20, 10))
    plt.title('Вейвлет преобразование Мексиканская шляпа', fontsize=30)
    plt.imshow(cwtmatr, extent=[-1, vj, -1, 1], cmap='PRGn', aspect='auto', vmax=abs(cwtmatr).max(),
               vmin=-abs(cwtmatr).max())
    plt.xlabel('Дни', fontsize=20)
    plt.ylabel('Амплитуда', fontsize=20)
    plt.show()
# -----------------------------------------------------------------------------------------------------------------

ui.mhatpush.clicked.connect( mhat )

# -----------------------------------------------------------------------------------------------------------------
def morlet():
    vj = len(peredacha())
    widths = np.arange(1, 41)
    cwtmatr = signal.cwt(peredacha(), signal.gaussian, widths)
    fig = plt.figure(figsize=(20, 10))
    plt.title('Вейвлет преобразование Морлет', fontsize=30)
    plt.imshow(cwtmatr, extent=[-1, vj, -1, 1], cmap='PRGn', aspect='auto', vmax=abs(cwtmatr).max(),
               vmin=-abs(cwtmatr).max())
    plt.xlabel('Дни', fontsize=20)
    plt.ylabel('Амплитуда', fontsize=20)
    plt.show()
# -----------------------------------------------------------------------------------------------------------------

ui.morletpush.clicked.connect( morlet )



#Выход из приложения
sys.exit(app.exec_())
