import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
import numpy as np


# membuat window
wx = 6          # lebar
wy = 3          # tinggi
wr = wx / wy    # aspect ratio

fig = plt.figure(figsize= (wx, wy))
fig.canvas.manager.set_window_title("Image GUI")

a = 0.08
b = 0.15
w = 0.5
h = 0.8

# axis chart
axChart = fig.add_axes( [a, b, w, h] )

# axis button
axBtn = fig.add_axes([2*a + w, h, w/2, 0.1])
btnRand = Button(ax=axBtn, label="New Data")

axRst = fig.add_axes([2*a + w, h-0.15, w/2, 0.1])
btnRst = Button(ax=axRst, label="Reset")

# R2
axR2 = plt.axes([2*a + w, h-0.5, w/2, 0.08])
axR2.axis('off')
axR2.text(x=0, y=0, s="R2: ")
txR2 = axR2.text(x=0.25, y=0, s="0")

# MSE
axMSE = plt.axes([2*a + w, h-0.6, w/2, 0.08])
axMSE.axis('off')
axMSE.text(x=0, y=0, s="MSE: ")
txMSE = axMSE.text(x=0.25, y=0, s="0")

# initial data
X = np.random.rand(10)
X =np.round(np.linspace(1, 5, 10), 2)
Y = -2*np.random.rand(10)
Y = np.round(Y + 2*X+1, 2)

ylim0, ylim1 = -1, 12
axChart.set_ylim([ylim0, ylim1])

# functions

def new_random_data(e):
    global X, Y
    X = np.random.rand(10)
    X = np.round(np.linspace(1, 5, 10), 2)
    Y = -2*np.random.rand(10)
    Y = np.round(Y + 2*X+1, 2)
    [b0, b1, err_, R2, MSE] = reg_lin(X, Y)
    sldB0.set_val(b0)
    sldB1.set_val(b1)
    drawchart(X, Y, b0, b1, err_, R2, MSE)
    

def reg_lin(x, y, b0=None, b1=None):
    x_ave = np.mean(x)
    y_ave = np.mean(y)

    xs = x - x_ave
    ys = y - y_ave

    if(b1==None):
        b1 = np.sum(xs * ys) / np.sum(xs * xs)
    if(b0==None):
        b0 = y_ave - b1 * x_ave  

    err_ = y - (b0 + b1 * x)

    MSE = np.sum(err_ * err_) / np.size(err_)
    R2 = 1 - np.sum(err_ * err_) / np.sum(ys * ys)

    return(b0, b1, err_, R2, MSE)


def drawchart(x, y, b0, b1, err_, R2, MSE):
    x_min = np.min(x)
    x_max = np.max(x)
    xa = np.linspace(x_min, x_max, 50)
    ya = b0 + b1 * xa

    axChart.clear()
    axChart.set_ylim([ylim0, ylim1])
    axChart.plot(x, y, '.r')
    axChart.plot(xa, ya, 'b')
    
    for i, er in zip(np.arange(len(err_)), err_):
        axChart.plot([x[i], x[i]], [y[i], y[i]-er], 'g')

    txR2.set_text(np.round(R2, 3))
    txMSE.set_text(np.round(MSE, 3))

    plt.pause(0.01)
    

# axis slider
(b0, b1, err_, R2, MSE) = reg_lin(X, Y)

axB0 = fig.add_axes( [2*a + w, h-0.3, w/2, 0.08] )
sldB0 = Slider(ax=axB0, label="B0", valmin=b0-2, valmax=b0+2, valinit=b0)

axB1 = fig.add_axes( [2*a + w, h-0.4, w/2, 0.08] )
sldB1 = Slider(ax=axB1, label="B1", valmin=b1-2, valmax=b1+2, valinit=b1)

drawchart(X, Y, b0, b1, err_, R2, MSE)


def setB0(e):
    b0 = sldB0.val
    (b0, b1, err_, R2, MSE)=reg_lin(x=X, y=Y, b0=b0)
    drawchart(X, Y, b0, b1, err_, R2, MSE)


def setB1(e):
    b1 = sldB1.val
    (b0, b1, err_, R2, MSE)=reg_lin(x=X, y=Y, b1=b1)
    drawchart(X, Y, b0, b1, err_, R2, MSE)



def reset(e):
    (b0, b1, err_, R2, MSE)=reg_lin(x=X, y=Y)
    sldB0.set_val(b0)
    sldB1.set_val(b1)
    drawchart(X, Y, b0, b1, err_, R2, MSE)


btnRand.on_clicked(new_random_data)
btnRst.on_clicked(reset)
sldB0.on_changed(setB0)
sldB1.on_changed(setB1)

plt.show()
