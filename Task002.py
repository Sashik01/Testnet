import numpy as np
import random as rd

def generation(): # Генерація матриці
    while True:
        a = int(input('Input size: '))
        b = int(input('Choose generation: 1 - auto, 0 - manually: '))
        if b == 0:
            return np.array([input().split() for _ in range(a)], dtype=int)
        elif b == 1:
            return np.array([[rd.randint(0, 1) for _ in range(a)] for _ in range(a)], dtype=int)
        else:
            print("Error. Try again.")

def infinity(): # Запуск
    flag = True
    while flag == True:
        a = int(input('Choose which iteration you want - finite or infinite? (1 - finite, 0 - infinite): '))
        if a == 1:
            a = generation()
            print("Your start matrix: ", a, sep='\n')
            print("Your finish matrix: ", finite(a), sep='\n') # Закінчення ітерацій
            flag = False
        elif a == 0:
            b = finite(generation())
            while True:
                b = finite(b)   # Нескінченна гра
        else:
            print("Error. Try again.")

def finite(matrix):  # Функція ходьби та підбору до умов
    rows = len(matrix)
    cols = len(matrix[0])

    def count_live_neighbors(x, y): # Функція рахування живих сусідів
        live_neighbors = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and matrix[new_x][new_y] == 1:
                live_neighbors += 1

        return live_neighbors

    for i in range(rows):
        for j in range(cols):
            live_neighbors = count_live_neighbors(i, j)

            if matrix[i][j] == 1:
                if 2 <= live_neighbors <= 3:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 0
            else:
                if live_neighbors == 3:
                    matrix[i][j] = 1
    return matrix

infinity()


