# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 01:05:42 2018

@author: Dr Ghost
"""
"""
Numpy Introduction

This is for 1 d (1 dimensional array)

Numerical Python, or "Numpy" for  short, is a foundational package on which many of the most common data science packages are built.
 Numpy provides us with high performance multi-dimensional arrays which we can use as vectors or matrices.

The key features of numpy are:

-------->   #ndarrays: n-dimensional arrays of the same data type which are fast and space-efficient.

There are a number of built-in methods for ndarrays which allow for rapid processing of data without using loops (e.g., compute the mean).

Broadcasting: a useful tool which defines implicit behavior between multi-dimensional arrays of different sizes.

 Vectorization: enables numeric operations on ndarrays.

 Input/Output: simplifies reading and writing of data from/to file.

"""
import numpy as np
x = np.array([3, 33, 333])  #create an array
print(x)

y = np.array([[3, 33, 333],[2,22,333]])   #creating the 2D array 
print(y)

y[1,1]  # printing the row and coloumn array


y[:,1] #printing the first colummn 



print(y)  #print the whole thing 
print(y[0,:])  #give the first row


y.shape  #size of the array



print(y[0,1]) # Slicing 
print(y[0]) # indexing
print(y[:,1])