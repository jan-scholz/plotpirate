#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from pylab import MaxNLocator
from random import *

bgcolor = np.array([255, 241, 223])/255.0
fill = np.array([224, 92, 128])/255.0
linecolor = np.array([213, 208, 191])/255.0
labelcolor = np.array([120, 117, 108])/255.0

plt.rcParams['savefig.facecolor'] = bgcolor

# parameters for random plot data
N = randint(8, 12)
x0 = randint(1950, 1995)
y_mu = gauss(0, 3)
y_sd = expovariate(0.7)

# parameterd for random plot style
plotwidth = 4 * 1.0
plotheight = 3 * 1.0
#plotwidth = 3 + gauss(0, 0.5)
#plotheight = 2 + gauss(0, 0.5)
barwidth_sd = plotwidth*2/N + gauss(0, 0.05)


X = np.linspace(start=x0, stop=x0+N-1, num=N).astype(int)
Y = [gauss(y_mu, y_sd) for x in range(N)]


fig = plt.figure(figsize=(plotwidth, plotheight), facecolor=bgcolor)
ax = plt.subplot(1,1,1, facecolor=bgcolor)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.tick_params(colors=labelcolor)

ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.yaxis.set_ticks_position('none')

ax.set_axisbelow(True)
ax.yaxis.grid(color=linecolor, linestyle=':', linewidth=1)

ax.bar(X, Y, width=0.5, facecolor=fill, edgecolor=fill)


# x-axis intercepting y=0
# adjust y ticks, steps=2
# add text boxes (title, subtitle, source)

# figure out position of most extreme x values
#   - move them inwards
#   - abbreviate them 2014 -> 14


# parametrize everything in external file (mplstyle?)

print(X)
print(Y)

#plt.show()
plt.savefig('foo.png'
    , dpi=60
    , bbox_inches='tight')
    #, pad_inches=0.5)

