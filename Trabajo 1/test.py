from re import X
from traceback import print_tb
from matplotlib import projections
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import time

x = np.linspace (0, 5, 50)
y = np.linspace (0, 5, 40)

X, Y = np.meshgrid (x, y)
Z = np.sin (X * 2 + Y) * 3 + np.cos (Y + 5)
print(y)