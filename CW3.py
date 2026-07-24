##file handeling
# file = open("D:\Git Work\Group, Name, Value.txt", "r")
# data = file.read()
# file.close()
# print(data)

# # create an empty class
# class EmptyClass:
#     pass

# # create a class which has a value
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Rahul", 20)
# print(s1.name, s1.age)

# # class with multiple objects
# class Student:
#     # The __init__ method is automatically called when a new object is created
#     def __init__(self, name, age, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#         self.age = age

## Create multiple instances of the Student class
# s1 = Student("Rahul", 20, 2009)
# s2 = Student("Priya", 22, 1009)
# print(s1.name, s1.age, s1.roll_no)
# print(s2.name, s2.age, s2.roll_no)

# Create a class which has basic attributes initialized via a constructor
# class Student:
#     # Display Method
#     def display(self):
#         print("Student Name :", self.name)
#         print("Roll Number  :", self.roll_no)
#         print("Final Marks  :", self.marks)
#         print("Course       :", self.course)
#         print("--------------------------")

## 5. Class with Dynamic Attributes & Methods
# student1 = Student()
# student2 = Student()
# student3 = Student()
# student4 = Student()

# # Assign Values to Objects
# student1.name = "Rahul"
# student1.roll_no = 101
# student1.marks = 92
# student1.course = "Python"
# student2.name = "Priya"
# student2.roll_no = 102
# student2.marks = 88
# student2.course = "Data Science"
# student3.name = "Aman"
# student3.roll_no = 103
# student3.marks = 95
# student3.course = "Artificial Intelligence"
# student4.name = "Sneha"
# student4.roll_no = 104
# student4.marks = 90
# student4.course = "Machine Learning"
# # Display Student Details
# student1.display()
# student2.display()
# student3.display()
# student4.display()

# # swapping two numbers without using third variable
# def swap(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     print("Swapped number:", a, b)
# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# swap(a, b)

# # Parent Class (Base Class)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_person(self):
#         print("Name        :", self.name)
#         print("Age         :", self.age)

# #Child Class (Derived Class)
# class Student(Person):
#     def __init__(self, name, age, roll_no, marks):
#         # Call Parent Constructor
#         super().__init__(name, age)
#         # Child Class Variables
#         self.roll_no = roll_no
#         self.marks = marks

#     def show_student(self):
#         print("Roll Number :", self.roll_no)
#         print("Marks       :", self.marks)

# # Create Object
# student1 = Student("Shivansh Verma", 20, 101, 92)
# # Display Data
# print("Student Information")
# print("---------------------------------------------")
# student1.show_person()  # Parent Class Method
# student1.show_student()  # Child Class Method
