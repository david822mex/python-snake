import json

FILE_PATH = "data/example.json"
my_dict = {
    "1": {
        "id": 1,
        "name": "name",
        "email": "email",
        "password": "password"
    },
    "2": {
        "id": 2,
        "name": "name2",
        "email": "email2",
        "password": "password2"
    }
}
# 1. read a json file, using json.load()
try:
    with open(FILE_PATH, "r") as file:
        users_json = json.load(file)

# 2. write a json file, using json.dump(obj, filepath, indent, ...other args), it will overwrite the file
except FileNotFoundError:
    with open(FILE_PATH, "w") as file:
        json.dump(obj=my_dict, fp=file, indent=4)

# 3. add a new entry and write to the file
else:
    with open(FILE_PATH, "w") as file:
        new_entry = {
            "3": {
                "id": 3,
                "name": "name3",
                "email": "email3",
                "password": "password3"
            }
        }
        users_json.update(new_entry)
        json.dump(obj=users_json, fp=file, indent=4)

# 4. change the 2nd user name to "Mary"
finally:
    with open(FILE_PATH, "r") as file:
        my_users = json.load(file)
        my_users["2"]["name"] = "Mary"
        my_users["3"]["name"] = "Ben"

    with open(FILE_PATH, "w") as file:
        json.dump(my_users, file, indent=4)

# 5. delete the 1st user
    with open(FILE_PATH, "r") as file:
        my_users = json.load(file)
        # del my_users["1"]

    with open(FILE_PATH, "w") as file:
        json.dump(my_users, file, indent=4)
