"""
# f - strings
greeting = 'Helmo Rise'
print(greeting)

print(f'Our Dark Lord {greeting}')

variable1 = 'Our Dark Lord'
variable2 = 'of the internet'

print(f'{variable1} {variable2} {greeting}')
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# definition statements
m = eval(input('given mass:'))  # mass kg
v = eval(input('given velocity:'))  # velocity m/s
t = eval(input('given time:'))  # time s


def acceleration(time, velocity):
    a = velocity / time
    return a


def force(mass, acceleration):
    f = mass * acceleration
    return f


print(f' given a mass {m}kg, and an acceleration {acceleration(t, v)}m/s/s, we get a force \
     {force(m, acceleration(t, v))}N')
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# creating a for  loop and using the loop to create graphs (plotting)
import numpy as np
import matplotlib.pyplot as plt

n = eval(input('input number:'))
array = np.arange(0, n + 1, 1)  # start value, stop - 1 value, increments
list_of_numbers = []  # empty list where we will assign the y values to

for index in array:
    y = index ** 2
    list_of_numbers.append(y)  # will append the calculated y value into the empty list
print(list_of_numbers)

# plotting the list
plt.plot(array, list_of_numbers, color='green')  # x-values, y-values, color, label
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('this is a title')
plt.legend('y = x^2', loc='lower right')
plt.savefig('y = x^2')  # will save the graph as a png file in the repository
plt.show()  # displays the graph
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# another for loop
import numpy as np
n = eval(input('enter n value:'))
n_values_array = np.linspace(0, n, n + 1)  # starting value, ending value, how many values
initial_value = 0
for i in n_values_array:
    equation = i * (i + 1) / 2
    initial_value += i  # adds and sets equal to the index value
    print(initial_value, equation)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# matrices
import numpy as np

matrix_A = np.array([[1, 0], [0, 1]])  # arrays are great for calculating
# ^we have a nested list in the array to make the identity matrix
matrix_B = np.array([[2, 4], [6, 8]])  # example matrix


def matrix_stuff(A, B):
    add = np.add(A, B)  # will add the matrix elements correctly
    subtract = np.subtract(A, B)
    multiply = np.multiply(A, B)  # will only multiply the elements, to matrix multiply, use np.dot for dot product
    divide = np.divide(A, B)  # only divides the elements
    return add, subtract, multiply, divide


print(f'The addition of A and B is:')
print(f'{matrix_stuff(matrix_A, matrix_B)[0]}')  # throwing in [0] will only print the 0 item in the return list
# at this point, the new matrix of A + B will print out
# but if we want to extract a specific term from the matrix we can use a for loop
# lets grab the first term in all four matrices in matrix_stuff
first_terms_list = []
for i in matrix_stuff(matrix_A, matrix_B):  # we are calling the function, so we cannot use A and B
    first_terms = i[0][0]  # will grab the term in the 0 row and 0 column
    first_terms_list.append(first_terms)  # will append the first terms to the empty list above

print(first_terms_list)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# looking at the __main__function as well as importing functions from other code
from functions import pizza, pie  # created a functions.py and wrote a def statement called pizza and pie

if __name__ == "__main__":  # not really sure what this is for but its here bc convention
    # for pizza
    meat = input('meat choice:')  # we are entering words not number so eval is not necessary
    cheese = input('kind of cheese:')
    print(pizza(meat, cheese))
    # for pie, but we didnt define the arguments like in pizza, defined it in the print statement
    print(pie(input('pie filling:')))
"""
