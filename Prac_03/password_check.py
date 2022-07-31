"""
CP1404
Prac 03
Junyao Nan
13940686
"""

# print("please enter the least 6 password")
#
# password = input("please enter your passwords:")
# while len(password) < 6:
#     password = input("please enter your passwords:")
# print("*" * len(password))

def main():
    print("please enter the password at least 6 characters")
    password = get_password()
    print_password(password)

def get_password():
    password = input("please enter your password:")
    while len(password) < 6:
        print("please enter the password at least 6 characters")
        password = input("please enter your password:")
    return password

def print_password(password):
    print("*" * len(password))

main()