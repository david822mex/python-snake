# hello123456
import pandas

# read the csv
data = pandas.read_csv("data/titanic.csv")

# choose a column, case sensitive. The two following expressions are the same.
survived = data["Survived"]
survived2 = data.Survived

# choose multiple columns, put column names in a list, thus the double [[]]
selected = data[["Survived", "Age"]]

# more than one filter, each filter should be inside (),
# and then join the filters with | (or) , & (and)
age_above_35 = selected[(selected.Age > 35) & (selected.Survived > 0)]

# .head() to show a few rows to visualize the data
# print(selected.head())

# .shape, to show the number of rows and columns
# print(selected.shape)

# loc operator for column name
names_of_people_over_35 = data.loc[data.Age > 35, "Name"]
# print(names_of_people_over_35)

# iloc operator for column index
# choose rows from 9 to 15, columns from 3 to 5
# print(data.iloc[9:15, 3:5])
# keep in mind that in a DataFrame, the first row is the column names
# and the first column is the index.


# .iloc[0] is the first item of data, not the row of column names
# the end is not included
#  so the first 10 records :
# print(data.iloc[0:10])

# to only show "Name", "Sex", "Age", use 3:6, because end is not included.
# print(data.iloc[0, 3:6])
