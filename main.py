import pandas as pd

data = pd.read_csv('D:\\iris.data', names=["sepal length", "sepal width", "petal length", "petal width", "class"])

#prints first 5 rows of the dataset.
print(data.head())


#prints a specific row from the dataset
print(data.iloc[45])

#prints a specific range from the dataset
print(data.iloc[90:98])

#prints a specific column of a specific row
print(data.at[69, "petal width"])

#printing all the row's petal width
for i in range(145):
    print(data.at[i, "petal width"])

#printing all the row's class
for i in range(145):
    print(data.at[i, "class"])

#adding a new row to the dataset
data.loc[len(data)] = [4.5,8,9,4,"iris_seo"]


#printing new dataset's tail
print(data.tail())

