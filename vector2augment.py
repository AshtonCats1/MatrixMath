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
A = [[3,2],[4,5]]
b = [1,2]
n = 5

#A is our matrix input and B is the solutions. So for 1x + 2y = 3, A is 1,2 and B is 3. B is in the format of a vector so b[1] will be the first solution etc.
def solve_system(A,b):
    num_rows = len(A)
    num_cols = len(A[0])
    augemented = np.zeros((num_rows,num_cols+1))
    for i in range(num_rows):
        for j in range(num_cols):
            augemented[i][j] = A[i][j]
        augemented[i][num_cols] = b[i]
    augemented[0] /= augemented [0][0]
    for i in range(1,num_rows):
        augemented[i] -= augemented[i][0] * augemented[0]
    augemented[1] /= augemented [1][1]
    for i in range (0,1): #the 1 in this loop will become j in your nested loops
        augemented [i] -= augemented[i][1] * augemented[i]
    for i in range (2,num_rows):
        augemented -= augemented[i][1] * augemented [i]
    print(augemented)

def solve_system2(A,b):
    num_rows = len(A)
    num_cols = len(A[0])
    augemented = np.zeros((num_rows,num_cols+1))
    for i in range (num_rows):
        for j in range(num_cols):
            augemented[i][j]= A[i][j]
        augemented[i][num_cols] = b[i]

    for i in range(num_rows):
            augemented[i] /= augemented [i][i]
            for k in range(num_rows):
                if k != i:
                    augemented [k] -= augemented[k][i] * augemented[i]
    print(augemented)                
solve_system2(A,b)

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














