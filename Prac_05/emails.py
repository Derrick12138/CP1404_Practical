def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = get_name_in_email(email)
        determine = input("Is your name {}? (Y/n)".format(name))
        if determine.upper() != "Y" and determine != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

        for email, name in email_to_name.items():
            print("{} ({})".format(name, email))


def get_name_in_email(email):
    name = email.split("@")[0]
    divide = name.split(".")
    user_name = " ".join(divide).title()
    return user_name


main()