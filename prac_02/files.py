
"""
# 1
"""
out_file = open("name.txt","w")
name = input("what's your name? : ")
print(name, file=out_file)
out_file.close()


"""
# 2
"""
in_file = open("name.txt", "r")
name = in_file.readline()
print("Your name is", name)
in_file.close()


"""
# 3
"""
in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
in_file.close()
print(first_number + second_number)


"""
# 4
"""
in_file = open("numbers.txt", "r")
total = 0
for i in in_file:
    number = int(i)
    total += number
in_file.close()
print(total)


