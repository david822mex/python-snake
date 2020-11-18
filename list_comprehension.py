import random
import pandas

old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
old_dict = {"Name": "David", "Age": 30, "Sex": "M"}

# 1.create a new list from old_list
new_list = [each * 2 for each in old_list]
print(new_list)

# 2. apply a condition with if statement
new_list2 = [each * 2 for each in old_list if each > 5 & each < 9]
print(new_list2)

# 3. create a dictionary from a list
new_dict = {"id" + str(each): each for each in old_list}
print(new_dict)

# 4. create a dictionary from another dict
new_dict2 = {"_" + key.lower(): str(value).upper() for (key, value) in old_dict.items()}
print(new_dict2)

print(random.randint(0, 2))  # both start and end are included

# 5. iterate from a DataFrame, using DataFrame.iterrows()
titanic_data = pandas.read_csv("data/titanic.csv")

for (index, row) in titanic_data.iloc[0:4, 4:5].iterrows():
    print(index, row)

# 6. create a new dictionary from a DataFrame:
people_survived = titanic_data[titanic_data["Survived"] > 0]
new_dict3 = {row.Name: row.Age for (index, row) in people_survived.iterrows()}
print(new_dict3)
