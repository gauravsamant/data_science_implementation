# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:45:59 2016

@author: GAURAVSAMANT
"""

###statistics

from collections import Counter
import vectors_ds as vec
import math

def mean(x):
    return sum(x)/len(x)
    
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2
    
    if n%2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint -1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi])/2
        
def mode(v):
    counts = Counter(v)
    max_counts = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() if count== max_counts]
    
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
    
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return vec.sum_of_square(deviations)/(n-1)
    
def standard_deviation(x):
    return math.sqrt(variance(x))
    
def covariance(x,y):
    n=len(x)
    return vec.dot(de_mean(x), de_mean(y))/(n-1)
    
def correlation(x,y):
    stddev_x = standard_deviation(x)
    stddev_y = standard_deviation(y)
    if stddev_x > 0 and stddev_y > 0 :
        return covariance(x,y)/stddev_x/stddev_y
    else:
        return 0