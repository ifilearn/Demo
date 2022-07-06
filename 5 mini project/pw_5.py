master_pwd = input("What is the master password? ")


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:",user, "Password:",passw)


def add():
    name  = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mod = input("Would you like to add a new password or view the existing ones (view / add or q to quit)? ")
    if mod == "q":
        break
    elif mod == "view":
        view()
    elif mod == "add":
        add()
    else:
        print("Invalid mode.")
        continue


