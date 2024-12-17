#!/usr/bin/python3

# Sometimes we want to draw attention to some feature of the plot, and the annotate() method provides helper functionality to make these annotations easy.

# In an annotation, there are main two points to consider:
# the location being annotated represented by the argument xy
# the location of the text xytext

import numpy as np
import matplotlib.pyplot as plt

# numpy-generated dataset for plotting
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2* np.pi *t)
line = plt.plot(t, s, lw=2)

for peak in range(1,5):
   plt.annotate('Pointy bits', xy=(peak, 1), xytext=(2.5, 1.5),
            arrowprops=dict(facecolor='#42f442', shrink=0.05),
            )
   
plt.ylim(-2,2)
plt.savefig("Chart_12.png",transparent=False)
