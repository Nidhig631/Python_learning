# getpass is module for user entering password.
# Here we are using the getpass module instead of the input function to make sure that the user doesn’t get to see what he/she write in the password field.
import getpass
database = {"nidhi": "123", "shruti": "112222"}
username = input("enter your name")
password = getpass.getpass("enter your password")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("enter your password again:")
            break
print("verified")
