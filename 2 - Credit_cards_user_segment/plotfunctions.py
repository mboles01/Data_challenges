#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:14:07 2019

@author: michaelboles
"""

# import packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# plot histogram

def plot_hist(data, textbox, props, xlabel, ylabel):
    fig, ax = plt.subplots(1,1,figsize=(7,7))
    #bins = np.arange(round(min(data),1), max(data) + binwidth, binwidth)
    props = dict(facecolor='white', alpha=1.0)

    ax.hist(data, edgecolor = 'black', facecolor = 'blue')
    
    plt.xlabel(xlabel, fontsize = 18, fontname = 'Helvetica')
    plt.ylabel(ylabel, fontsize = 18)
    ax.tick_params(axis = 'x', labelsize = 14); ax.tick_params(axis = 'y', labelsize = 14)
    
    for tick in ax.get_xticklabels():
        tick.set_fontname('Helvetica')
    for tick in ax.get_yticklabels():
        tick.set_fontname('Helvetica')
        
    ax.text(0.6, 0.95, textbox, transform = ax.transAxes, fontsize = 18, 
            fontname = 'Helvetica', verticalalignment = 'top', bbox = props)

    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['axes.unicode_minus'] = False
    plt.grid(); ax.grid(color=(.9, .9, .9)); ax.set_axisbelow(True)

    fig.tight_layout()
    
    import matplotlib.ticker as ticker
    plt.show()