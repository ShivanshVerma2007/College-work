# import pandas as pd
# import numpy as np
# data = {
#     "Name": ["Alice","Bob","Charlie","David","Eva","Frank","Grace","Hannah","Ian","Jack"],
#     "Roll No": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "Maths": np.random.randint(50, 100, size=10),
#     "Science": np.random.randint(50, 100, size=10),
#     "English": np.random.randint(50, 100, size=10),
#     "History": np.random.randint(50, 100, size=10),
#     "Geography": np.random.randint(50, 100, size=10)}

# df=pd.DataFrame(data)
# print(df.head(5))
# print(df.iloc[:10,[0,5]])
# print(df.loc[:10,["Roll No","English"]])
# print(df[:][::-1])
# print(df, "\n")
#adding new column
# df["Civics"] = np.random.randint(50, 100, size=10)
# print(df, "\n")
#add a new row at the end
# df.loc[len(df)]={"Name": "Kevin", "Roll No": 11, "Maths": 85, "Science": 90, "English": 88, "History": 92, "Geography": 80, "Civics": 75}
# print(df)
# print(pd.__version__)