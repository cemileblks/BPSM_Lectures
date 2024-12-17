#!/usr/bin/python3
# Working with multiple figures and axes

# Plot objects can hold multiple plots, and we use figure() to indicate which figure it is.

# figure(1) is created by default.

# Panels or subplots are generated using the subplot() command.

# subplot() specifies
# numrows,
# numcols,
# fignum
# where fignum ranges from 1 to numrows * numcols.

# The commas in the subplot command are optional if numrows * numcols is less than 10.

# subplot(211) is identical to subplot(2, 1, 1) and means 2 rows, 1 column, first panel.

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2* np.pi *t)

# two numpy ranges 
# arange returns evenly spaced values within a given interval.
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# First figure
plt.figure(1)

# First panel
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

# Second Panel
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

# Things to apply on the panel 212
plt.xlabel('X axis values')
plt.ylabel('Y axis values')
plt.savefig("Chart_08.png")
plt.show()
plt.close()

