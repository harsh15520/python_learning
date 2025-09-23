import getpass
users = {
    "user1": "pass123",
    "admin": "adminpass",
    "guest": "guestpass"
}
attempt=3
while(attempt>0):
    username = input("Enter username: ")
    password = input("enter password")
    if username in users and users[username]==password: 
        print("Login successful!")
        break
    else:
        attempt-=1
        print(f"Login failed.number of attempts left :{attempt}")
if attempt==0:
    print('login locked')
response=input("new user:Y/N \n")
if (response=='Y'):
    new_user=input("enter username")
    new_password=input('enter password')
    re_password=input("re-enter password")
    if(new_password==re_password):
        users[new_user]=new_password
    else:
        print('password not same')
elif(response=='N'):
    pass
else:
    print('invalid')
