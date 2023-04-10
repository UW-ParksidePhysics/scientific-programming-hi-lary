import numpy as np
import matplotlib.pyplot as plt

#matrix = np.array([[2, -1], [-1, 2]])
#print(f'A = {matrix}')
#print()

fives = np.ones(5)*2
#print(f'T-array = {fives}')
#print()

twos_matrix = np.diagflat(fives)
#print(f'T-matrix = {twos_matrix}')
#print()

negative_ones = np.ones(4)*-1
#print(f'N-array = {negative_ones}')
#print()

upper_negative_ones = np.diagflat(negative_ones, 1)
#print(f'N-upper = {upper_negative_ones}')
#print()

lower_negative_ones = np.diagflat(negative_ones, -1)
#print(f'N-lower = {lower_negative_ones}')
#print()

matrix = (1/(2*(1/6)**2))*(twos_matrix + upper_negative_ones + lower_negative_ones)
print(f'H = {matrix}')

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(f'lamda = {eigenvalues}')
print()
print(f'x = {eigenvectors}')
print()

x_values = np.linspace(1/6, 5/6, 5)
y_values = eigenvectors[4]
function = np.sqrt(2)*np.sin(np.pi * x_values)

plt.plot(x_values, y_values)
plt.show()
plt.plot(x_values, function)
plt.show()
