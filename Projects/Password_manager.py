from cryptography.fernet import Fernet
import os
# Fernet is an encryption library. It scrambles text so only someone with the right key can unscramble it.

# Function to generate and save a key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from the current directory
def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

# Check if key file exists, if not, create it
if not os.path.exists("key.key"):
    write_key()

# Initialize everything
master_pwd = input("What's your master Password? ").lower()
key = load_key()
fer = Fernet(key)

def view():
    if not os.path.exists('Password.txt'):
        print("No passwords stored yet.")
        return
        
    with open('Password.txt', 'r') as f:
        for line in f.readlines(): 
            data = line.rstrip()
            if "|" not in data:
                continue
            user, passw = data.split("|")
            # Decrypt: Encoded string -> Decrypt -> Decode to normal text
            decrypted_pwd = fer.decrypt(passw.encode()).decode()
            print("User:", user, "| Password:", decrypted_pwd)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('Password.txt', 'a') as f:
        # Encrypt: Password -> Encrypt -> Decode to string to save in file
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), or press q to quit? ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode!")
        continue
