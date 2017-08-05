import numpy as np
import math as mp
import matplotlib.pyplot as plt
from code import Differentiation

def main():
    t = [i for i in np.arange(0,10,.1)]
    alpha = .1
    graph = Differentiation(t,alpha)
    f1 = [mp.sin(i) for i in np.arange(0,10,.1)]
    f2 = [i**4 for i in np.arange(0,10,.1)]
    graph.plot_func(f1,f2)

if __name__ == "__main__":
    main();
