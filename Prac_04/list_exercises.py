def main():
    # 01 ask user print 5 number to display some result
    numbers = []
    print("please enter 5 numbers")
    for i in range(1, 6):
        number = int(input("Number {} >>> ".format(i)))
        numbers.append(number)

    print("the first number is :", numbers[0])
    print("the last number is :", numbers[-1])
    print("The smallest number is :", min(numbers))
    print("The largest number is :", max(numbers))
    print("The average of the numbers is :", sum(numbers) / len(numbers))
    print("----------------------------")

    # 02 ask user the name and check whether username are in the list
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Please enter your name \n>>>")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
