from cProfile import label
from operator import mod
from statistics import mode
from drawchart import drawChart
from turtle import title
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons
import numpy as np

# membuat window

radio_background = 'lightgoldenrodyellow'
wx = 8  # lebar window
wy = 4  # tinggi window

fig = plt.figure(figsize=(wx, wy))
fig.canvas.manager.set_window_title("Jumlah Reimann")

# membuat kotak tampilan foto
a = 0.06    # gap kiri
b = 0.1     # gap bawah
w = 0.6     # lebar
h = 0.8     # tinggi

# axes
axChart = fig.add_axes([a, b, w, h])
axChart.set_title("Jumlah Reimann")

axMode = fig.add_axes([2*a+w, 0.7, 0.8-w, h/4])
axMode.set_title("Mode")

axA = fig.add_axes([2*a+w, 0.5, 0.8-w, h/10])
axB = fig.add_axes([2*a+w, 0.42, 0.8-w, h/10])
axN = fig.add_axes([2*a+w, 0.3, 0.8-w, h/10])
axRes = fig.add_axes([2*a+w, 0.1, 0.8-w, h/8])

# widgets
sldrA = Slider(axA, valmin=-5, valmax=10, valinit=0, label='a')
sldrB = Slider(axB, valmin=-5, valmax=10, valinit=5, label='b')
sldrN = Slider(axN, valmin=1, valmax=100, valstep=1, valinit=5, label="N")

axRes.set_title("Hasil")

# SET MODE
axMode.set_facecolor(radio_background)
radio = RadioButtons(ax=axMode, labels=('left', 'mid', 'right'))

# ------------
chart = drawChart()
chart.plot(axis=axChart, x0=0, x1=5, N=8, pos='left')

# SET MODE
axMode.set_facecolor(radio_background)
radio = RadioButtons(ax=axMode, labels=('left', 'mid', 'right'))


def updatemode(label):
    chart.updatepos(pos=label)
    fig.canvas.draw()


radio.on_clicked(updatemode)


def sliderA(event):
    x0 = sldrA.val
    chart.plot(axis=axChart, x0=x0)


sldrA.on_changed(sliderA)       # x0


def sliderB(event):
    x1 = sldrB.val
    chart.plot(axis=axChart, x1=x1)


sldrB.on_changed(sliderB)       # x1


def sliderN(event):
    N = sldrN.val


sldrN.on_changed(sliderN)

plt.show()
