##importing different liberaries
# import keyword
# import numpy as np

## printing all the different keywords present in the python
# print(keyword.kwlist)

# # a=np.array([10,20,30,40])
# # print(a)

# # 1d array
# b = np.array([1, 2, 3, 4, 5, 6, 6])
# print("Array--->", b)
# print("Dimension--->", b.ndim)
# print("Size of array--->", b.size)
# print()

# # 2d array
# c = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 7, 8, 9]])
# print("Array--->", c)
# print("Dimension--->", c.ndim)
# print("Size of array--->", c.size)
# print()

# # 3d array
# d = np.array([[
#     [1, 2, 3, 4, 5],
#     [6, 7, 'A', 8, 9]]])
# print("Array--->", d)
# print("Dimension--->", d.ndim)
# print("Size of array--->", d.size)
# print("Shape of array--->", d.shape)
# print("Type of array--->", d.dtype)
# print()

# # 4d array
# e = np.array(
#     [[[[1, 2, 3, 4, 5], [6, 7, 10, 8, 9]], [[1, 2, 3, 4, 5], [6, 7, 1, 8, 9]]]])
# print("Array--->", e)
# print("Dimension--->", e.ndim)
# print("Size of array--->", e.size)
# print("Shape of array--->", e.shape)
# print("Type of array--->", e.dtype)
# print()

# # 5d array
# f = np.array([[[[
#     [1, 2, 3, 4, 5],
#     [6, 7, 'A', 8, 9]],
#     [[1, 2, 3, 4, 5],
#      [6, 7, 'A', 8, 9]],
#     [[1, 2, 3, 4, 5],
#      [6, 7, 'A', 8, 9]]]]])
# print("Array--->", f)
# print("Dimension--->", f.ndim)
# print("Size of array--->", f.size)
# print("Shape of array--->", f.shape)
# print("Type of array--->", f.dtype)

# # array of ones
# a = np.ones((5, 5))
# print(a)
# print()

# # identity of matrix
# b = np.eye(5)
# print(b)
# print()

# # empty array
# c = np.empty((2, 2))
# print(c)

##using arange function of the numpy
# a = np.arange(1, 7)
# print(a)
# b = np.arange(6, 12, 30)
# print(b)
# c = np.arange(12)
# print(c)

##using reshape function of the numpy
# d = c.reshape(3, 4)
# print(d)

##using slicing method of the list
# d = np.array([[
#     [1, 2, 3, 4, 5],
#     [6, 7, 'A', 8, 9]]])
# print("Array--->", d)
# print(d[0, 1, 2])

##using all the operators on the array
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([3, 4, 5, 6, 7])
# print(a+b)
# print(a*b)
# print(a/b)
# print(a**b)

# # Create a numpy array containing numbers from 1 to 20
# a = np.arange(1, 21)
# print(a)

# # create a 4x4 array of zero
# b = np.ones((4, 4))
# print(b)

# # create a 3x3 identity matrix
# c = np.eye(3)
# print(c)

# # find the shape of a 2x5 array
# d = np.array([[2, 3, 4, 5, 11], [1, 3, 7, 8, 0]])
# print(d.shape)

# # reshape an array of 12 elements into a 3x4 matrix
# d = np.arange(12)
# e = d.reshape(3, 4)
# print(e)

# import numpy as np
# s=np.linspace(0,20,5)
# print(s)

# num = [20, 45, 55, 60, 75]
# for i in range(0, 5):
#     if num[i] >= 50:
#         print(num[i])

# # Calculator
# n = int(input("Enter a number from 1 to 10:"))
# m = int(input("Enter a number from 1 to 10:"))
# ch = input("Enter the mathematical operator:")
# if ch == "+":
#     print("Addition:", n + m)
# elif ch == "-":
#     print("Subtration:", n - m)
# elif ch == "%":
#     print("Remainder:", n % m)
# elif ch == "/":
#     print("Division:", n / m)
# elif ch == "*":
#     print("Multiplication:", n * m)
# elif ch == "**":
#     print(n, "to the power", m, "is:", n**m)
# else:
#     print("Invalid character.")
