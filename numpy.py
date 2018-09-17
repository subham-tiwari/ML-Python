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

print("size of the array")
y.shape  #size of the array



print(y[0,1]) # Slicing 
print(y[0]) # indexing
print(y[:,1])

print("how to create a matrix of same value like one two's and three's")

one=np.zeros([2,3])
one

nines=np.full([3,3] , 9)
print(nines)


#how to make 2D array of matrix

x1=np.array([[1,2,3,4,5],[5,1,8,2,3]])
x2=np.array([[1,2,3,4,6],[6,7,8,3,10]])


print(x1)
print("")
print(x2)

#add the matrices 
x3=x1+x2
x4=np.add(x1,x2)

#subtract 
x5=x2-x1
x6=np.subtract(x4,x1)

#Randon numbers to generate with a given size of the matrix as well 

randm=np.random.random((1,2))
randm


#arrange the matrix

arrange=np.arange(0,12)

#Apply condition to the values of the matrix 

ex1=np.random.random((2,3))
ex1

checkgreator=(ex1>1)
checkgreator

checklesser=(ex1<0.5)


#Get the meaen value of the matrix is easy by using the function 

meanarray=np.mean(checklesser)
meanarray
meanofx1row=np.mean(x1,axis=0)

#Sort the X1

sortx1=x1.sort()

#median of the given numbers
medianx1=np.median(x1 , axis=1)
medianx1

#Unique values in the matrix

uniquex1=np.unique(x1)
print(uniquex1)
