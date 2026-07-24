##importing different libraries
# import pandas as pd
# import numpy as np

##performing different types of mathematical functions on the array
# a = np.array([1, 4, 90, 16])
# print("Absolute value--->", np.abs(a))
# print("Square root--->", np.sqrt(a))
# print("Exponential--->", np.exp(a))
# print("Natural log--->", np.log(a))
# print("Sine--->", np.sin(a))
# print("Cosine--->", np.cos(a))
# print("Tangent--->", np.tan(a))

# # random
# print(np.random.rand(5))
# # random intigers
# print(np.random.randint(1, 100, 10))
# # random matrix
# print(np.random.randint(1, 50, (3, 4)))

# marks = np.array([75, 80, 90, 85, 95])
# # Average
# print("Mean--->", np.mean(marks))
# # Maximum
# print("Maximum--->", np.max(marks))
# # Minimum
# print("Minimum--->", np.min(marks))
# # Sum
# print("Sum--->", np.sum(marks))
# # Median
# print("Medium--->", np.median(marks))
# # Standard Deviation
# print("Standard Deviation--->", np.std(marks))

## Generate 50 random salaries between 10,000 and 100,000
# salary = np.random.randint(10000, 100000, 50)

## Sort the salaries in ascending order
# print("Salary before increment--->", np.sort(salary))
# print("--------------------------------------------------------------------------")
# print("Sum--->", np.sum(salary))
# print("--------------------------------------------------------------------------")

## Find and print the maximum salary
# m = np.max(salary)
# print("Maximum--->", m)
# print("--------------------------------------------------------------------------")

## Find and print the minimum salary
# mi = np.min(salary)
# print("Minimum--->", mi)
# print("--------------------------------------------------------------------------")

##Difference between the maximum and the minimum salary
# print("Difference between max to the min is", m - mi)
# print("--------------------------------------------------------------------------")

##Average salary
# print("Average Salary--->", np.mean(salary))
# print("--------------------------------------------------------------------------")

##Median Of the salary
# print("Median--->", np.median(salary))
# print("--------------------------------------------------------------------------")

##Salary after increment
# inc = salary + 0.05
# print("Salary after increment--->", inc)

# # create a file of 10 students each having name, roll no and marks of 5 subjects
# data = {
#     "Name": [
#         "Alice",
#         "Bob",
#         "Charlie",
#         "David",
#         "Eva",
#         "Frank",
#         "Grace",
#         "Hannah",
#         "Ian",
#         "Jack"],
#     "Roll No": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "Maths": np.random.randint(50, 100, size=10),
#     "Science": np.random.randint(50, 100, size=10),
#     "English": np.random.randint(50, 100, size=10),
#     "History": np.random.randint(50, 100, size=10),
#     "Geography": np.random.randint(50, 100, size=10),
# }

##Creating dataframe
# df = pd.DataFrame(data)
# print("Student Data:\n", df)

##Creating series
# se = pd.Series([1, 3, 4, 5, 6], index=["A", "b", "c", "D", "F"])
# print(se)

##reading csv
# df = pd.read_csv("record.csv")
# print(df)
# df = pd.read_csv("emp.csv")
# print(df)
# print("--------------------------------------------------------------------------")

##first 2 rows
# print(df.head(2))
# print("--------------------------------------------------------------------------")

##last 2 rows
# print(df.tail(2))
# print("--------------------------------------------------------------------------")

##printing columns
# print(df.columns)
# print("--------------------------------------------------------------------------")

##printing the shape
# print(df.shape)
# print("--------------------------------------------------------------------------")

##printing the index
# print(df.index)
# print("--------------------------------------------------------------------------")

##printing the informtions
# print(df.info())
# print("--------------------------------------------------------------------------")

##describing dictionary
# print(df.describe())
# print("--------------------------------------------------------------------------")

##using loc and iloc functions
# print(df.loc[0])
# print("--------------------------------------------------------------------------")
# print(df.iloc[1])

# student = {
#     "Roll_No": [0, 1, 2, 3, 4],
#     "Name": ["Ram", "Shayam", "Geeta", "Seeta", "Tom"],
#     "Marks": [11, 15, 20, 19, 18],
# }
# df = pd.DataFrame(student)
# print(df)
##creating a new csv file
# df.to_csv("newfile.csv", index=False)
