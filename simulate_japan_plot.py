#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

bg = np.array([255, 241, 223])/255.0
fill = np.array([224, 92, 128])/255.0
linecolor = np.array([213, 208, 191])/255.0
labelcolor = np.array([120, 117, 108])/255.0

X = np.arange(2009, 2014, step=0.25)
Y = np.array([0.1, 7, 6, 5, 6, -2, -8, -2, 11, 0.5, 4, -2, -2.5, -0.5, 5, 4, 2, -0.5, 6, -8])


fig = plt.figure(figsize=(5,3), facecolor=bg)
ax = plt.subplot(1,1,1, facecolor=bg)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.tick_params(colors=labelcolor)

ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")
ax.yaxis.set_ticks_position('none')

ax.set_axisbelow(True)
ax.yaxis.grid(color=linecolor, linestyle=':', linewidth=1)

ax.bar(X, Y, width=0.2, facecolor=fill, edgecolor=fill)


# x-axis intercepting y=0
# move y ticks to right
# adjust y ticks, steps=2
# vertical dotted lines at 4, 8, 12
# remove frame
# add text boxes (title, subtitle, source)


# figure out position of most extreme x values
#   - move them inwards
#   - abbreviate them 2014 -> 14


# parametrize everything in external file (mplstyle?)


plt.show()


