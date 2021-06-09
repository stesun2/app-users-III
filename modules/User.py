# Your User class goes here
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, '..\\csv\\users.csv')
class User:
    def __init__(self, name, email, age):
        self.name  = name
        self.email = email
        self.age   = age

    @classmethod
    def get_all_users(cls):
        with open(path, 'r') as users_file:
            users = csv.DictReader(users_file)
            users_list = []
            for user in users:
                users_list.append(User(user['name'], user['email'], user['age']))
            return users_list

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_age(self):
        return self.age

    # write user

    