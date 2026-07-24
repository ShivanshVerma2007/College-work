##printing
# name = "Shivansh Verma"
# age = 20
# print("Name: ", name)
# print("Age: ", age)

##creating sum
# num1 = 5
# num2 = 9
# print("Sum:", num1+num2)

##Swapping two numbers with the help of third variable
# num3 = num1
# num1 = num2
# num2 = num3
# print("Swapped Numbers are: ", num1, num2)

##printing the data type
# print(type(num1))
# num4 = 3.14
# print(type(num4))
# print(type(name))

##printing the list
# l = [1, 2, 3, 4, 5, 6]
# print(type(l))

##printing bool
# a = bool(4050)
# print(type(a))

##modulus operator
# a = 5 % 7
# print("Remainder: ", a)

##checking the two numbers
# if num1 == num2:
#     print("Equal!!")
# else:
#     print("Not Equal!!!")

# if num3 > 100:
#     print("Greater than 100!!")
# else:
#     print("Not greater than 100!!")

##square of the number
# num5 = num1*num1
# print("Square:", num5)

##even or odd numbers
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # greater or smaller
# b = 10
# if a > b:
#     print("a is greater than b.")
# else:
#     print("b is greater than a.")

# # check whether a number is positive, negative or zero
# num = float(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# # example of function
# def greet(name):
#     print("Hello, " + name + "!")
# greet("Alice")
# greet("Bob")
# greet("Charlie")

# # calculate the lenth of your name
# def name_length(name):
#     return len(name)
# print("Length of your name:", name_length("Shivansh"))

##operations appling on the list
# lst = [1, 2, 3, 4, 5, 6]
# print("List:", lst)
# lst.append(10)
# print("New list1:", lst)
# lst.remove(10)
# print("New list2:", lst)
# lst[2] = 88
# print("New list3:", lst)

# # to print pyramid of stars
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print("  ", end=" ")
#     for k in range(1, 2 * i):
#         print("* ", end=" ")
#     print()

##tupples
# tupple = ("aaa", "baaa", "saaa", "daaa")
# print(tupple)

# # Factorial Function
# def factorial(n):
# fact = 1
# for i in range(1, n + 1):
# fact *= i
# return fact
# print(factorial(5))

# #For loop
# for i in range(0, 20):
#     if (i % 2 == 0):
#         print(i)

# sum = 0
# for i in range(1, 100):
#     sum = sum + i
# print("Sum of 1 to 100 is ", sum)

# for i in range(1, 11):
#     print("5 * ", i, " = ", 5*i)

# # wap a program of four function calculator
# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x / y

# # create a list of 5 fruits and print
# fruits = ["apple", "banana", "orange", "grape", "mango"]
# print("Fruits:", fruits)

# # print the first and last element of the list
# print("First fruit:", fruits[0])
# print("Last fruit:", fruits[-1])

# # add a new student name in the list
# fruits.append("pineapple")
# print("Fruits after adding pineapple:", fruits)

# # remove "Banana" from the list
# fruits.remove("banana")
# print("Fruits after removing banana:", fruits)

# # find the length of the list
# print("Length of the list:", len(fruits))

# # sort the list in ascending order
# fruits = ["apple", "banana", "orange", "grape", "mango"]
# fruits.sort()
# print("Fruits after sorting:", fruits)

# # sort the list in descending order
# fruits.sort(reverse=True)
# print("Fruits after sorting in descending order:", fruits)

# # find the largest number in a list
# numbers = [5, 10, 2, 8, 3]
# largest = max(numbers)
# print("Largest number in the list:", largest)

# # print every item in a list using a for loop
# for fruit in fruits:
#     print(fruit)

# # print the second element of a tuple
# tupple = ("aaa", "baaa", "saaa", "daaa")
# print("Second element of the tuple:", tupple[1])

# # count how many times 5 appears in a tuple
# tupple2 = (1, 5, 3, 5, 2, 5, 4)
# count_5 = tupple2.count(5)
# print("Number of times 5 appears in the tuple:", count_5)

# # convert a tuple to a list
# tupple_to_list = list(tupple)
# print("Tuple converted to list:", tupple_to_list)

# # write a function to add two numbers
# def add_numbers(x, y):
#     return x + y
# result = add_numbers(5, 3)
# print("Sum of 5 and 3 is:", result)

# # write a function to find the square of a number
# def square(num):
#     return num * num
# result_square = square(4)
# print("Square of 4 is:", result_square)

# # write a function that checks whether a number is even or odd
# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# result_even_odd = check_even_odd(7)
# print("7 is:", result_even_odd)

# # write a function that prints a student's name
# def print_student_name(name):
#     print("Student's name is:", name)
# print_student_name("Alice")

# # write a function to calculate the average of three numbers
# def average_of_three(x, y, z):
#     return (x + y + z) / 3
# result_average = average_of_three(5, 10, 15)
# print("Average of 5, 10, and 15 is:", result_average)

##dictionary
# dic = {"Fruits": ["Apple", "Banana", "Pineapple", "Watermelon",
#                   "Papaya", "Orange"], "Students": ["Ram", "Shyam", "Seeta", "Geeta"]}
# print(dic)

# # to read a file
# file = open("Messi.txt", "r")
# print(file.read())
# file.close()

# # create a pyramid with its mirror image
# row = 5
# for i in range(1, row+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
# for i in range(row-1, 0, -1):
#     for j in range(0, i):
#         print("*", end=" ")
#     print()

# # Simple Notes App
# while True:
#     note = input("Enter Note (type exit to stop): ")
#     if note.lower() == "exit":
#         break
#     with open("notes.txt", "a") as file:
#         file.write(note + "\n")
# print("All notes saved successfully.")
