# -*- coding: utf-8 -*-

import numpy as np

f = open("inputdata.txt" , "r")

filestring = f.read()
filelist = filestring.split("\n") #this will split by rows
f.close()
matrix = []
scalars = []
matrices = []
for s in filelist:
    parts = s.split(":")
    label = parts[0]
    data = parts[1]
    if label == "scalar":
        scalar_value = float(data)
        scalars.append(scalar_value)
    elif label == "vector":
        row = data.split(",") #this will split by collums
        float_array = np.zeros(len(row))
        for i in range (len(row)):
            float_array[i] = float(row[i])
        matrix.append(float_array) 
    elif label == "matrix":
        rows = data.split(";") #splits matrix into rows (vectors)
        current_matrix = []
        for row_string in rows:
            row_values = row_string.split(",")
            float_array = np.zeros(len(row_values))
            for i in range (len(row_values)):
                float_array[i] = float(row_values[i])
            current_matrix.append(float_array)

        matrices.append(current_matrix)
            

        
    #turn the string into floats using float()
print(matrices[0])
vector1 = matrix[0]
vector2 = matrix[1]
A = [[3,2],[4,5]]
b = [1,2]
n = len(matrix[0])
c = np.eye(n)
d = np.eye (n)
e = np.zeros((n,n))
#A is our matrix input and B is the solutions. So for 1x + 2y = 3, A is 1,2 and B is 3. B is in the format of a vector so b[1] will be the first solution etc.
def solve_system2(A,b):
    num_rows = len(matrix)
    num_cols = n
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
    return(augemented)                
#solve_system2(A,b)

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

def mat_mult(a,b,c):
    for i in range (n):
        for j in range (n):
            temp = 0.0
            for k in range (n):
                temp += a[i][k] * b[k][j]
            c[i][j] = temp
    return (c)

#running addition of vectors
result = matrix[0]
for i in range(1, len(matrix)):
    result = add(result, matrix[i], n)
print ("addition of all vectors", result)
#running subtraction of vectors
result = matrix[0]
for i in range(1, len(matrix)):
    result = subtract(result, matrix[i], n)
print ("subtraction of all vectors:", result)
#running vector multiplication
result = matrix[0]
for i in range(len(matrix)):
    result = scalar_product(scalars[0], matrix[i], n)
    print("vector", i, "multiplied by", scalars[0], "=", result)
    
#running dot product
result = matrix[0]
# Check how many vectors we have
if len(matrix) == 2:
    # Only run if exactly 2 vectors
    result = dot_product(matrix[0], matrix[1], n)
    print("dot product is", result)
else:
    print("cannot do dot product of more than 2 vectors")

#Tests
#print(add(vector1, vector2, 3))
#print(subtract(vector1, vector2, 3))
#print(scalar_product(5, vector1, 3))
#print(dot_product(vector1, vector2, 3))














