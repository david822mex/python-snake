import pandas as pd
import matplotlib.pyplot as plt

# Udemy. Section 72
# the csv file contains: each month("DATE), each language("TAG") has how many posts("POSTS").


df = pd.read_csv("data/QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)
# set the header=0 to replace the original header.
# print(df.head())

# get an idea what the df looks like: .head(), .tail(), .shape
# print(df.shape)

# count how many entries in each column.
# print(df.count())

# the total number of posts per language?
group_tag = df.groupby("TAG").sum()
# print(group_tag)

# how many months does each language exist?
# we see that "go", "swift" have less months because they didn't exist yet when the record was made.
months_exist = df.groupby("TAG").count()
# print(months_exist)

# change the format of "DATE" column
df["DATE"] = pd.to_datetime(df["DATE"])
# print(df.DATE)

# pivot the table
pivoted = df.pivot(index="DATE", columns="TAG", values="POSTS")
# print(pivoted.javascript)

# convert "NaN" to 0
pivoted.fillna(0, inplace=True)
# print(pivoted)

# how to check if there are still NaN data?
check_nan = pivoted.isna().values.any()
# print(check_nan)

# now we plot: popularity of each language through time. Y = number of posts, X = time
# Take "Javascript" and "Python" for example
# plt.plot(pivoted.index, pivoted.javascript, label="Js")
# plt.plot(pivoted.index, pivoted.python, label="Py")


# to show all of the columns in one graph, use a for in loop:
# plt.figure(figsize=(16, 10))  # size of the fig
# plt.xlabel('Date', fontsize=14)
# plt.ylabel('Number of Posts', fontsize=14)
# plt.ylim(0, 35000)
# for column in pivoted.columns:
#     plt.plot(pivoted.index, pivoted[column], label=column)
# plt.legend()  # show legend
# plt.show()  # finally show the plot

# how to smooth the lines.
# rolling mean: Essentially we calculate the average in a window of time
# and move it forward by one observation at a time. the bigger the window, the smoother the line is.
roll_pivoted = pivoted.rolling(window=3).mean()
plt.plot(roll_pivoted.index, roll_pivoted.javascript)
plt.show()
