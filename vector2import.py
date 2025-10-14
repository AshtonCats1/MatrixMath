# -*- coding: utf-8 -*-

import numpy as np

f = open("inputdata.txt" , "r")

filestring = f.read()
filelist = filestring.split("\n") #this will split by rows
f.close()
matrix = []
for s in filelist:
    row = s.split(",") #this will split by collums
    float_array = np.zeros(len(row))
    for i in range (len(row)):
        float_array[i] = float(row[i])
    matrix.append(float_array)
    #turn the string into floats using float()

vector1 = matrix[0]
vector2 = matrix[1]
n = 5

def add(a, b, n):
    #Adds vectors a and b, which are both of length n
    c = np.zeros(n)
    for i in range (n):
        c[i] = a[i] + b[i]
    return c
    
    #Your code here 
    

def subtract(a, b, n):
    #Subtracts vectors a and b, which are both of length n
    c = np.zeros(n)
    for i in range (n):
        c[i] = a[i] - b[i]
    return c
    
    #Your code here
    


def scalar_product(scalar, vector, n):
    #Returns the product of scalar * vector.
    #the vector has a length of n
    c = np.zeros(n)
    for i in range (n):
        c[i] = scalar * vector[i]
    return c
    #Your code here
    
    
def dot_product(a, b, n):
    #Returns the dot product of vectors a and b, which are both of length n
    temp = 0.0
    for i in range (n):
        temp += a[i] * b[i]
    return temp
    #Your code here
    


#Tests
print(add(vector1, vector2, 3))
print(subtract(vector1, vector2, 3))
print(scalar_product(5, vector1, 3))
print(dot_product(vector1, vector2, 3))














