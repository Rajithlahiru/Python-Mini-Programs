from cryptography.fernet import Fernet


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer: Fernet = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readline():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "|password", passw)
            fer.decrypt(passw.encode()).decode()


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()) + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view them or press q to quit(view/add or q)"
    )
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode")
        continue
