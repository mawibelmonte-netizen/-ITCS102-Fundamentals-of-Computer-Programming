import getpass

loginattempt = 0

username = "imaw"
password = "1024"

while True:
    lusername = input("Username: --> ")
    lpassword = input("Password: --> ")

    if lusername == username and lpassword == password:
        print("Login Successfully...")
        print("Login Attempts: ", loginattempt)
        break
    else:
        print("Login Unsuccessfully...")
        loginattempt = loginattempt + 1