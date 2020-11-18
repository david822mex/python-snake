# 4 stages:

# 1. try

# 2. except, this part of code runs if the "try" part fails.

# 3. else, this part of code runs if the "try" part goes through without error.

# 4. finally, no matter what happens, this part of code always gets executed.




# example:

try:
    file = open("file.txt")
    file_content = file.read()
    dict1 = {"key": "value"}
    key = dict1["alkdj"]
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("created")
except KeyError as err_msg:
    print("The key: " + str(err_msg) + "does not exist")

else:
    file.write("hello")
finally:
    print("what is in file: " + file_content)
    file.close()


# raise my own error
raise TypeError("My made up error")


