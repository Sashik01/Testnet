import numpy as np

def generation_A():  #Генерація матриці А
    a = int(input('Input size of matrix A(n x n): '))
    return np.array([input().split() for _ in range(a)], dtype=float)

def generation_B():  #Генерація матриці В
    b = int(input('Input size of matrix B(n x 1): '))
    return np.array([float(input()) for _ in range(b)]).reshape(b, 1)


def inv_matrix(matrix):  #Генерація матриці А^(-1)
    if (np.linalg.det(matrix) == 0):                 #Перевірка детермінанту
        print("The determinant of the matrix = 0, so it is impossible to create an inverse matrix")
    else:
        return (np.linalg.inv(matrix))

def function(matrix_a, matrix_b):  # Множення матриць
    return (matrix_a @ matrix_b).transpose()


A = function(inv_matrix(generation_A()), generation_B())
print(f'X(T) = {A}')


