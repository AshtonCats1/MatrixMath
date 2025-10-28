# -*- coding: utf-8 -*-

import numpy as np

f = open("inputdata.txt" , "r")

filestring = f.read()
filelist = filestring.split("\n") #this will split by rows
f.close()
matrix = []
scalars = []
matrices = []
systems = []
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
            row_values = row_string.split(",") #this will split by collumns
            float_array = np.zeros(len(row_values))
            for i in range (len(row_values)):
                float_array[i] = float(row_values[i])
            current_matrix.append(float_array)

        matrices.append(current_matrix)
    elif label == "system":
        rows_system = data.split(";") #splits by rows
        A_matrix = []
        b_vector = []
        for row_string in rows_system:
            parts = row_string.split("=") #splitting by equals sign to get the variables and solutions
            variables = parts[0] #this is for storing the like 3x +2y part
            solution = parts[1] #this is for storing the = 5 part

            variables_values = variables.split(",") #splits by collums (you know the drill by now this is like the 4th comment ive made on the same line of code)
            float_array = np.zeros(len(variables_values))
            for i in range (len(variables_values)):
                float_array[i] = float(variables_values[i])
            A_matrix.append(float_array)

            b_vector.append(float(solution))
        systems.append((A_matrix, b_vector))


n = len(matrix[0])

#A is our matrix input and B is the solutions. So for 1x + 2y = 3, A is 1,2 and B is 3. B is in the format of a vector so b[1] will be the first solution etc.
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
    return(augemented)
                
def mat_determ(a):
    rows = len(a) #finding the lengths of rows and collums so we can check how big they are and if they are square matrices
    cols = len(a[0])

    if rows != cols:
        print("Can only find determints that are square")
        return None
    
    if rows != 2 and rows != 3:
        print("Can only find determints that are 2x2 or 3x3")
        return None
    if rows == 2:
        det = a[0][0] * a[1][1] - a[0][1]*a[1][0]
        return det
    if rows == 3:
        det = a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[1][0]*(a[0][1]*a[2][2]-a[0][2]*a[2][1])+a[2][0]*(a[0][1]*a[1][2]-a[0][2]*a[1][1]) #looks like a lot of code but its just doing normal determint stuff (a1* (b2*c3 etc)), nothing fancy
        return det
    
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
    
    
def dot_product(a, b, n):
    #Returns the dot product of vectors a and b, which are both of length n
    temp = 0.0
    for i in range (n):
        temp += a[i] * b[i]
    return temp

def mat_mult(a, b):
    #gets dimensions of rows and collums in a and b
    rows_a = len(a)           # Number of rows in a
    cols_a = len(a[0])        # Number of columns in a
    rows_b = len(b)           # Number of rows in b
    cols_b = len(b[0])        # Number of columns in b
    #see if cols_a is equal to rows_b because if it isnt you cant multiply matrices
    if cols_a != rows_b:
        print("matrices cannot be multiplied")
        return None
    
    # Result will be rows_a × cols_b
    c = np.zeros((rows_a, cols_b))
    
    for i in range(rows_a):
        for j in range(cols_b):
            temp = 0.0
            for k in range(cols_a):
                temp += a[i][k] * b[k][j]
            c[i][j] = temp
    return c

def mat_add(a, b):
    #gets dimensions of rows and collums in a and b and see if rows_b is equal because if it isnt you cant multiply matrices
    rows_a = len(a)           # Number of rows in a
    cols_a = len(a[0])        # Number of columns in a
    rows_b = len(b)           # Number of rows in b
    cols_b = len(b[0])        # Number of columns in b

    if rows_a != rows_b or cols_a != cols_b:
        print("matrices cannot be added")
        return None
    
    c = np.zeros((rows_a, cols_b))
    
    for i in range(rows_a):
        for j in range(cols_a):
            c[i][j] = a[i][j] + b[i][j]
    return c

def mat_subtract(a, b):
    #gets dimensions of rows and collums in a and b and see if rows_b is equal because if it isnt you cant multiply matrices
    rows_a = len(a)           # Number of rows in a
    cols_a = len(a[0])        # Number of columns in a
    rows_b = len(b)           # Number of rows in b
    cols_b = len(b[0])        # Number of columns in b

    if rows_a != rows_b or cols_a != cols_b:
        print("matrices cannot be subtracted")
        return None
    
    c = np.zeros((rows_a, cols_b))
    
    for i in range(rows_a):
        for j in range(cols_a):
            c[i][j] = a[i][j] - b[i][j]
    return c

def mat_mult_scalar(a, b):
    #gets dimensions of rows and collums in a 
    rows_a = len(a)           # Number of rows in a
    cols_a = len(a[0])        # Number of columns in a

    c = np.zeros((rows_a, cols_a))
    
    for i in range(rows_a):
        for j in range(cols_a):
            c[i][j] = a[i][j] * b
    return c
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
#running matrix multiplcation
result = matrices[0]
for i in range(1, len(matrices)):
    result = mat_mult(result, matrices[i])
print("multiplying all matrices =", result)
#running matrix addition
result = matrices[0]
for i in range(1, len(matrices)):
    result = mat_add(result, matrices[i])
print("adding all matrices =", result)
#running matrix subtraction
result = matrices[0]
for i in range(1, len(matrices)):
    result = mat_subtract(result, matrices[i])
print("subtracting all matrices =", result)
#running multiplying a matrix by a scalar
result = matrices[0]
for i in range(len(matrices)):
    result = mat_mult_scalar(matrices[i], scalars[0])
    print("multipying matrix", [i], "by", scalars[0],"=", result)
#running solve system
for i in range(len(systems)):
    A_matrix, b_vector = systems[i]
    result = solve_system2(A_matrix,b_vector)
    
    solutions = []
    for row in result:
        solutions.append(row[-1])
    print("Solution for system", [i], "=", solutions)
#running finding determinits
for i in range(len(matrices)):
    det = mat_determ(matrices[i])
    print("the determinent of matrix", [i], "=", det)