import numpy as np
import matplotlib.pyplot as plt

matrix = np.array([[2, -1], [-1, 2]])
print(f'A = {matrix}')
print()

matrix_dimention = 2
twos = np.ones(matrix_dimention)*2
print(f'T-array = {twos}')
print()

twos_matrix = np.diagflat(twos)
print(f'T-matrix = {twos_matrix}')
print()

negative_ones = np.ones(1)*-1
print(f'N-array = {negative_ones}')
print()

upper_negative_ones = np.diagflat(negative_ones, 1)
print(f'N-upper = {upper_negative_ones}')
print()

lower_negative_ones = np.diagflat(negative_ones, -1)
print(f'N-lower = {lower_negative_ones}')
print()

matrix = twos_matrix + upper_negative_ones + lower_negative_ones
print(f'M = {matrix}')

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(f'lamda = {eigenvalues}')
print()
print(f'x = {eigenvectors}')
print()
