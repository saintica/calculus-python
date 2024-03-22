import numpy as np


def f(x): return np.sin(x)/(1+x**2)


class drawChart:

    def __init__(self, axis) -> None:
        self.axis = axis
        self.x0 = 0
        self.x1 = 5
        self.N = 10
        self.dx = 0.5
        self.pos = 'left'

    def plot(self):
        self.axis.clear()
        self.dx = (self.x1 - self.x0)/self.N

        X = np.linspace(self.x0, self.x1, 10*self.N+1)
        x = np.linspace(self.x0, self.x1, self.N+1)

        xl = x[:-1]                 # x left
        xm = (x[:-1] + x[1:])/2     # x center
        xr = x[1:]

        self.modedict = {'left': xl, 'mid': xm, 'right': xr}

        xdata = self.modedict[self.pos]
        ydata = f(xdata)
        self.axis.plot(X, f(X), lw=2, color='red')

        self.bars = self.axis.bar(xdata, ydata, width=self.dx, alpha=0.2,
                                  align='edge', edgecolor='b')

        self.dots, = self.axis.plot(xdata, ydata, 'b.', markersize=100/self.N)

        # calculate the result
        xdata = self.modedict[self.pos]
        sum = np.round(np.sum(f(xdata))*self.dx, 8)

        return sum

    def setX0(self, x0):
        self.x0 = x0

    def setX1(self, x1):
        self.x1 = x1

    def setN(self, N):
        self.N = N

    def updatepos(self, label):
        self.pos = label
        xdata = self.modedict[self.pos]
        ydata = f(xdata)
        for bar, h in zip(self.bars, ydata):
            bar.set_height(h)

        self.dots.set_xdata(xdata)
        self.dots.set_ydata(ydata)

        sum = np.round(np.sum(f(xdata))*self.dx, 8)
        return sum
