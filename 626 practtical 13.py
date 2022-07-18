# -*- coding: utf-8 -*-
#NAME : NEHAAL ANIL PANDEY
#ROLL NO. : 626
#BATCH : F1
#DATE : 19/08/2021.

#PRACTICAL: Write a NumPy program for Plotting and analyzing data.
#INPUT:
import numpy as np                                                 # importing numpy
from matplotlib import pyplot as plt                    #using matplotlib (a plotting library) we are importing pylot(a module in matplotlib)
x= np.array([1,4,9,16,25,36,49,64,81,100])      # inserting all the values of x axis in the form of an array.
y= np.array([1,2,3,4,5,6,7,8,9,10])                     # inserting all the values of x axis in the form of an array.
plt.title("No. vs Its Square")                #inserting title for the graph 
plt.xlabel("x axis")                                
plt.ylabel("y axis")                               #inserting labels for axes
plt.plot(x,y, "x-")                                  #plot() fucntion plots the graph with a solid line (shortcut is "-" with "x" saped markers)
plt.show()                                            # show() function to display the graph which is plotted.
