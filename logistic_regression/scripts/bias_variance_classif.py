import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def plot_class_one():
    x = [1, 2.1, 3, 5, 6, 7, 5.5]
    y = [0.05, 0.1, 0.8, 0.9, 0.2, 0.7, 0.5]
    

    plt.plot(x, y, "X", color = 'r')
    plt.xlim(0,10)
    plt.ylim(0,5)
    plt.show()
    
plot_class_one()
