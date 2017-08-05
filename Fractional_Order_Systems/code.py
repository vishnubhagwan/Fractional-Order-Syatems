import numpy as np
import matplotlib.pyplot as plt

class Differentiation:
    def __init__(self, t, alpha):
        self.t = t
        self.alpha = alpha

    def derivative(self, y):
        t = self.t
        alpha = self.alpha
        h = t[2] - t[1]
        dy = [0]*len(y)
        dy[1] = 0
        y = y[:]
        t = t[:]
        w = [0]*len(y)
        w[1] = 1
        for i in range(2,len(t)):
            w[i] = w[i-1]*(1-(alpha+1)/float(i-1))
        for i in range(2,len(t)):
            for j in range(1,i):
                for k in xrange(i,0,-1):
                    dy[i] += w[j]*y[k]/(h**alpha)
        return dy

    def plot_func(self, y1, y2):
        t = self.t
        for k in range(8):
            self.alpha += .1
            dy1 = self.derivative(y1)
            dy2 = self.derivative(y2)
            plt.hold(True)
            plt.subplot(211).set_title("y=x^2")
            plt.plot(t,dy1)
            plt.axis([0,10,0,20])
            plt.subplot(212).set_title("y=x^4")
            plt.plot(t,dy2)
            plt.axis([0,10,0,20])
        plt.show()
