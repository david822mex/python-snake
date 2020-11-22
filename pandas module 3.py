import pandas as pd
import matplotlib.pyplot as plt


colors_df = pd.read_csv("data/colors.csv")
sets_df = pd.read_csv("data/sets.csv")

#  how many unique colors, answer is: 135
how_many_colors = colors_df["name"].nunique()
# print(how_many_colors)

# how many transparent colors, answer is 28
# the following are 3 ways to do that:
# 1st
n_trans_color = colors_df[colors_df["name"].str.contains("Trans")].count()
# print(n_trans_color)

# 2nd
# print(colors_df.groupby("is_trans").count())

# 3rd
# print(colors_df["is_trans"].value_counts())






# In which year were the first LEGO sets released and what were these sets called?
sort_year = sets_df.sort_values("year")
first_set = sort_year.iloc[0]
# print(first_set)

# How many different products did the LEGO company sell in their first year of operation?
sets_1949 = sets_df[sets_df["year"] == 1949]
# print(sets_1949.nunique())

# What are the top 5 LEGO sets with the most number of parts?
sets_with_most_parts = sets_df.sort_values("num_parts", ascending=False)
# print(sets_with_most_parts.head())

# create a new Series, that has the years as index, and the number of sets as value
sets_by_year = sets_df.groupby("year").count()
# print(sets_by_year)

# plot "sets_by_year", without the data from "2020" or "2021"
n_of_years = sets_df["year"].nunique()
# data_until_2019 = sets_by_year.iloc[0:n_of_years - 2]
# print(n_of_years)
# print(data_until_2019)
# plt.plot(data_until_2019.index, data_until_2019.name)
# plt.show()

# calculate the number of different themes by year
themes_by_year = sets_df.groupby("year").agg({"theme_id": pd.Series.nunique})
# print(themes_by_year)

# plot themes_by_year, without the latest 2 years
# plt.plot(themes_by_year.index[:-2], themes_by_year.theme_id[:-2])
# plt.show()

# how to plot the "sets_by_year" and "themes_by_year" on the same chart? They have different scale,
# so we should have 2 y-axis in the chart.
# ax1 = plt.gca()
# ax2 = ax1.twinx()
# ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
# ax2.plot(themes_by_year.index[:-2], themes_by_year.theme_id[:-2], color="b")
# ax1.set_xlabel("Year")
# ax1.set_ylabel("Num of Sets", color="g")
# ax2.set_ylabel("Num of Themes", color="b")
# plt.show()

# Create a Pandas Series called "parts_per_set"
# that has the year as the index and
# contains the average number of parts per LEGO set in that year:
parts_per_set = sets_df.groupby("year").agg({"num_parts": pd.Series.mean})
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])


# which theme has the most sets? show their names
sets_per_theme = sets_df["theme_id"].value_counts()
sets_per_theme = pd.DataFrame({"id": sets_per_theme.index, "set_count": sets_per_theme.values})
# print(sets_per_theme)
themes = pd.read_csv("data/themes.csv")
merged = pd.merge(sets_per_theme, themes, on="id")
print(merged)

