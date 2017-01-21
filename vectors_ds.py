# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:18:06 2016

@author: GAURAVSAMANT
"""
import math

def vector_add(v,w):
    return [v_i+w_i for v_i, w_i in zip(v,w)]
    
def vector_sub(v, w):
    return [v_i-w_i for v_i, w_i in zip(v, w)]
    
def vector_sum(vectors):
    result=vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result
    
def scalar_multiply(c, v):
    return [c*v_i for v_i in v]
    
def vector_mean(vectors):
    n=len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v,w):
    return sum(v_i*w_i for v_i, w_i in zip(v,w))
    
def sum_of_square(v):
    return dot(v,v)
    
def magnitude(v):
    return math.sqrt(sum_of_square(v))
    
def squared_distance(v,w):
    return sum_of_square(vector_sub(v,w))
    
def distance(v,w):
    return magnitude(vector_sub(v,w))
    
#### matrix calculations
    
def shape(a):
    num_row= len(a)
    num_col = len(a[0] if a else 0)
    return num_row, num_col
    
def get_row(a,i):
    return a[i]
    
def get_col(a,j):
    return [a_i[j] for a_i in a]
    
def make_matrix(num_row, num_col, entry_fn):
    return [[entry_fn(i,j) for j in range(num_col)] for i in range(num_row)]
    
def is_diagonal(i,j):
    return (1 if i==j else 0)
    
def make_identity(i,j):
    return make_matrix(i,j,is_diagonal)