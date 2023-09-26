## User class
## Author: Atanas Chelibashki
## Date: 26/09/2023
## Version 1.0
## Description: This class is used to create a user object

class User:
    def __init__(self,id, username, password, first_name, last_name, email, role):
        self.id = id
        self.username = username
        self.password = password
        self.fname = first_name
        self.lname = last_name
        self.email = email
        self.role = role # user privileges (admin=1, user=0)

    # Add other methods as needed

    def __str__(self):
        return f"{self.username} {self.password} {self.fname} {self.email}"

    def __repr__(self):
        return f"{self.username} {self.password} {self.fname} {self.email}"

    def get_id(self):
        return self.id
    
    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_full_name(self):
        return self.fname + "" + self.lname

    def set_fname(self, fname):
        self.fname = fname

    def set_lname(self, lname):
        self.lname = lname

    def set_email(self, email):
        self.email = email

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password



