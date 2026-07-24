##importing all liberaries
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

##reading csv file
# df = pd.read_csv("null.csv")
# print(df)

# print("--------------------------------Filtering Data------------------------------------------")
# print(df[(df["Salary"]>40000) & (df["Department"]=="HR")])

# print("--------------------------Sorting Data------------------------------------------------")
# print(df.sort_values("Salary",ascending=False))

# print("--------------------------Renaming Data------------------------------------------------")
# print(df.rename(columns={"Employee_ID":"ID"}))

# print("--------------------------Describing Data------------------------------------------------")
# print(df.describe())

##reading csv file
# df = pd.read_csv("employee_data_20_rows.csv")
# print(df)

# print("------------------------------First three rows--------------------------------------------")
# print(df.head(3))

# print("------------------------------Last three rows--------------------------------------------")
# print(df.tail(3))

# print("------------------------------Shape of the rows--------------------------------------------")
# print(df.shape)

# print("------------------------------Columns of the dataframe--------------------------------------------")
# print(df.columns)

# print("------------------------------Index of the DataFrame--------------------------------------------")
# print(df.index)

# print("------------------------------Information Of the DataFrame--------------------------------------------")
# print(df.info())

# print("------------------------------Description of the dataframe--------------------------------------------")
# print(df.describe())

# print("------------------------------Sorting the dataframe according to ID Column--------------------------------------------")
# print(df.sort_values("ID",ascending=False))

# print("------------------------------Grouping according to the department column --------------------------------------------")
# total=df.groupby("Department")["Salary"].sum()
# print(total)

# df=pd.read_csv("null.csv")
# print(df)
##Using different types of functions
# print("--------------------------------------------------------------------------")
# print(df.isnull())
# print("--------------------------------------------------------------------------")
# print(df.isnull().sum())
# print("--------------------------------------------------------------------------")
# print(df.fillna(0))
# print("--------------------------------------------------------------------------")
# print(df.fillna("Unknown"))
# print("--------------------------------------------------------------------------")
# df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
# print(df)

# df=pd.read_csv("1000_people.csv")
# print(df)

##Plotting Graphs
# x=[1,3]
# y=[10,15]
# plt.plot(x,y)
# plt.show()

##===================================
##Plotting Different types of Charts
##====================================

## Data Preparation
# emp=["Ram","Shayam","Geeta","Seeta"]
# sal=[160000,250000,470000,300000]
# sal=[16000,25000,47000,30000]

## Plotting Commands (Various Chart Types)
# data=np.array([[10,21,45,67,89],[21,54,87,98,54],[34,29,58,71,99]])
# plt.plot(emp,sal,linewidth=2,linestyle="-.",color="black",marker="x",label="A")
# plt.plot(emp,sal,linewidth=2,linestyle="-.",color="black",marker="x",label="B")
# plt.bar(emp,sal,color="orange")
# plt.barh(emp,sal,color="orange")
# plt.pie(sal, labels=emp)
# plt.scatter(emp,sal)
# plt.hist(emp)
# plt.imshow(data)
# plt.colorbar()

##Chart Formatting and Display
# plt.xlabel("Employees names")
# plt.ylabel("Salary")
# plt.title("Yearly salary")
# plt.legend()
# plt.show()

