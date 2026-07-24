##importing library
# import math

# # Example1
# name1 = "Rahul"
# name2 = "Shyam"
# age1 = 20
# age2 = 30
# name1 = name1.upper()
# name2 = name2.lower()
# print("Name: ", name1, "Age: ", age1)
# print("Name: ", name2, "Age: ", age2)

# # Example2
# name3 = name1+" "+name2
# print(name3)

# # Example3
# print(name3[:5])
# print(name3[6:])

# # Example4
# a = 2
# b = 3
# print(a == b)

# # Exaple5
# user_input = input("Enter something: ")
# print("Type of input: ", type(user_input))

# # Example6
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))

# if a > b:
#     print("a is greater than b.")
# else:
#     print("b is greater than a.")

# # Example7
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # Example8
# num = float(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# # Example9
# year = int(input("Enter year:"))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# # Example10
# num = 7
# is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
# print("Prime" if is_prime else "Not Prime")

# # Example11
# n = 5
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# # Example12
# print("Factorial of 5:", math.factorial(5))

# # Example13
# num = 5
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# # Example14
# for i in range(1, 11):
#     print(i, end=" ")

# # Example15
# marks = float(input("Enter the marks of the student:"))
# if (marks > 90):
#     print("Grade A")
# elif (marks > 80 and marks <= 90):
#     print("Grade B")
# elif (marks > 70 and marks <= 80):
#     print("Grade C")
# else:
#     print("Grade D")
