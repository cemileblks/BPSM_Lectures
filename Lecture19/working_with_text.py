#!/usr/bin/python3

# Working with text()
# There is an excellent summary of options given at:

# http://matplotlib.org/api/pyplot_summary.html

# The text() command can be used to add text in an arbitrary location, and the xlabel(), ylabel() and title() are used to add text in the indicated locations

# A simple numpy-generated dataset of IQ values for plotting

import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# using plt.hist and it has so many options check using help(plt.hist)

n, bins, patches = plt.hist(x, 50, density=True, facecolor='#ee42f4', alpha=0.75)

# n: is the number of counts (normally!) in each bin of the histogram, this time it is density
# bins: is the left hand edge of each bin
# patches: the individual patches used to create the histogram, e.g a collection of rectangles
# facecolor: what colour do we want? can use hex values

# Axis labelling etc
plt.xlabel('Intelligence quotient value')
plt.ylabel('Probability')
plt.title('Histogram of IQ')

# Axis ranges, tick marks (x1,x2 y1,y2)
plt.axis([40, 160, 0, 0.03])

# Annotation, note use of special np characters \mu and \sigma
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')

# Additional region added on chart (vertical line)
plt.axvline(x=mu+(2*sigma),linewidth=4, color='r')

# Annotation for region added on chart
plt.text(mu+(2.1*sigma), .025, r'$\mu + 2\sigma$')

# Put a default grid on the chart
plt.grid(True)

# Could have changed things, e.g colour of the 9th rectangle...
# plt.setp(patches[10], facecolor='g')

# Save and show
plt.savefig("Chart_11.png",transparent=False)
plt.show()