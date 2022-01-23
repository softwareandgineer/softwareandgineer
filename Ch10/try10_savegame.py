import json


class User:
    def __init__(self, name, score, level):
        self.name = name
        self.score = score
        self.level = level

    def get_description(self):
        description = f" name = {self.name}, score = {self.score}, level = {self.level}"
        return description

    def save(self, filename):
        dict = {"name": self.name, "score": self.score, "level": self.level}
        with open(filename,'w') as user_data:
            json.dump(dict, user_data)

    def load(self, filename):
        with open(filename) as user_data:
            dict = json.load(user_data)

        self.name = dict["name"]
        self.score = dict["score"]
        self.level = dict["level"]

name = input("Input your username:")

filename = name + ".json"

user = User(name, 0, 0)

try:
    user.load(filename)
    print(f"{user.get_description()}")
    print(f"Welcome back, {name}!")
    user.level += 69420
    user.score += 1000000
    user.save(filename)
except FileNotFoundError:
    user = User(name, 0, 1)
    user.save(filename)
    print("Welcome New User")
