# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LinearRegression

# # 1. Create a sample dataset
# data = {'Years_of_Experience': [1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7, 
#                             3.9, 4.0, 4.0, 4.1, 4.5, 4.9, 5.1, 5.3, 5.9, 6.0],
#     'Salary': [39343, 46205, 37731, 43525, 39891, 56642, 60150, 54445, 64445, 57189,
#                63218, 55794, 56957, 57081, 61111, 67938, 66029, 83088, 81363, 93940]}

# # Convert data into a pandas DataFrame
# df = pd.DataFrame(data)

# # Separate Features (X) and Target (y)
# X = df[['Years_of_Experience']] 
# y = df['Salary']

# # Initialize and train the model using ONLY LinearRegression
# model = LinearRegression()
# model.fit(X, y)

# # Take user input for years of experience
# user_input = input("Enter years of experience: ")
# user_exp = float(user_input)

# # Pass the input as a DataFrame with the same column name to avoid the warning
# new_experience = pd.DataFrame([[user_exp]], columns=['Years_of_Experience'])

# # Predict the salary
# predicted_salary = model.predict(new_experience)

# # Display the results using string concatenation and commas
# print("\nPredicted Salary for", user_exp, "years of experience: $", round(predicted_salary[0], 2))