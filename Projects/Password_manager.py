master_pwd = input("What's your master Password? ").lower()

def view():
    pass
def add ():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('Password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n") # Notice the \n!


while True:
    mode = input("Would you like to add a new password or view existing onces(View/Add) or 'q' to quite ? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")
        continue
