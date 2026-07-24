## ==========================================
## Importing Machine Learning Libraries
## ==========================================

# Import NumPy for creating and manipulating arrays
# import numpy as np

# Import KMeans for grouping data points (Unsupervised Learning)
# from sklearn.cluster import KMeans

# Import LinearRegression for predictive modeling (Supervised Learning)
# from sklearn.linear_model import LinearRegression


## ==========================================
## Linear Regression (Supervised Learning)
## ==========================================

# # Define the independent variable (features) as a 2D array
# # Example: Square footage of houses (1000, 1200, etc.)
# x = [[1000], [1200], [1500], [1800]]

# # Define the dependent variable (target) as a 1D array
# # Example: Corresponding house prices in Lakhs
# y = [40, 50, 65, 80]

# # Initialize the Linear Regression model
# model = LinearRegression()

# # Train (fit) the model using the provided x (features) and y (targets)
# model.fit(x, y)

# # Predict the target value for a new unseen data point (e.g., a 1600 sq ft house)
# # The input must be a 2D array, matching the shape of 'x'
# prediction = model.predict([[1600]])

# # Print the predicted result
# # prediction[0] extracts the value from the returned prediction array
# print("Prediction Price:", prediction[0], "Lakh")

# ## ==========================================
# ## K-Means Clustering (Unsupervised Learning)
# ## ==========================================

# # Create a dataset with distinct groupings of data points
# # Notice that [2, 3] & [3, 4] are geometrically grouped together, 
# # and [10, 12] & [11, 13] form a separate group.
# data = np.array([[2, 3], [3, 4], [10, 12], [11, 13]])

# # Initialize the KMeans clustering model
# # n_clusters=2: Instructs the algorithm to find exactly 2 clusters/groups
# # random_state=42: Sets a seed for the random number generator to ensure consistent results every run
# model = KMeans(n_clusters=2, random_state=42)

# # Train the model to find the natural clusters in the unlabeled data
# model.fit(data)

# # Print the resulting cluster assignments
# # model.labels_ returns an array assigning each data point to cluster '0' or cluster '1'
# print("Cluster Labels:")
# print(model.labels_)