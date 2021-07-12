import hashlib
import os


num=int(input("No of user you want to input:-"))
users={}

#add user

for i in range(num):
    username=input("username:-")
    password=input("password:-")

    salt=os.urandom(32)
    key=hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,100000)
    users[username]={'salt':salt,'key':key}

print("Now time to verify!!!!")
for i in range(num):

    username=input("username:-")
    password=input("password:-")

    salt=users[username]['salt']
    key=users[username]['key']
    new_key=hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,100000)

    if new_key==key:
        print("Password is Correct")
    else:
        print("Password is Incorrect")
