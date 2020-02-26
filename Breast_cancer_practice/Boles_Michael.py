#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:29:04 2020

@author: michaelboles
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro
from scipy.stats import skew
from scipy.stats import kurtosis

# Import data set
import os
os.chdir('/Users/michaelboles/Michael/Coding/2020/Insight/Data challenges/Breast_cancer_practice')
data_raw = pd.read_csv('./breast-cancer-wisconsin.txt')



# get most common values
values = pd.DataFrame()
for column in data_raw:
    value_counts = data_raw[column].value_counts() 
    values[str(column)] = pd.Series(value_counts.index[:10])


# get corresponding counts
counts = pd.DataFrame()
for column in data_raw:
    value_counts = data_raw[column].value_counts() 
    values[str(column)] = pd.Series(value_counts[0])
    print(value_counts[:9])



# convert all columns to integer data type
data_numeric = data_raw.apply(pd.to_numeric, errors='coerce').dropna().astype(int)

# plot distributions
from plotfunctions import plot_hist

for column in data_numeric.columns[1:]:
    print(column)
    data = data_numeric[str(column)]

    # textbox
    average = round(np.nanmean(data), 2)
    median = round(np.nanmedian(data), 2)
    stdev = round(np.std(data), 2)
    props = dict(facecolor='white', edgecolor='none', alpha=0.67, boxstyle='square, pad=1')
    textbox = str(column) + ' \nAverage = %.1f \nMedian = %.1f \nStdev = %.1f' % (average, median, stdev)
    
    print(average, median, stdev)
    
    # binwidth = 1
    xlabel = 'Value'
    ylabel = 'Counts'

    plot_hist(data, textbox, props, xlabel, ylabel)
    
    