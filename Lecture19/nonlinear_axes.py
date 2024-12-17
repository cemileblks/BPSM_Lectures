#!/usr/bin/python3

# plt supports not only linear axis scales, but also logarithmic and logit ( log(z / (1 - z)) for any value between 0 and 1 ) scales. 
# This is commonly used if data span many orders of magnitude.

import numpy as np
import matplotlib.pyplot as plt

# An example of four plots of the same data but different scales for the y axis
# Make up some data in the interval 0 .. 1
y = np.random.normal(loc=0.5, scale=0.4, size=1000) 

y = y[(y > 0) & (y < 1)]

y.sort()
x = np.arange(len(y))

# Plot with various axes scales
plt.figure(figsize=(20,10))

# Linear
plt.subplot(221)
plt.plot(x, y, 'r-',linewidth=3.0)
plt.yscale('linear')
plt.title('LINEAR')
plt.grid(True)

# Log
plt.subplot(222)
plt.plot(x, y, 'g-',linewidth=3.0)
plt.yscale('log')
plt.title('LOG')
plt.grid(True)

# Symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean(), 'm-',linewidth=3.0)
plt.yscale('symlog', linthreshy=0.05)
plt.title('SYMLOG')
plt.grid(True)

# Logit: log-odds, or the logarithm of the odds of z/(1 - z)
plt.subplot(224)
plt.plot(x, y, 'b-',linewidth=3.0)
plt.yscale('logit')
plt.title('LOGIT')
plt.grid(True)

# Save and show
plt.savefig("Chart_13.png",transparent=True)
plt.show()
