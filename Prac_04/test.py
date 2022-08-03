# date_string = input("Enter DOB (d/m/y)")
# parts = date_string.split("/")  # this will be a list of strings
# my_dob = (int(parts[0]), int(parts[1]), int(parts[2]))
# print(my_dob)


def fn1(arg1=[], arg2=27):
    arg1.append(arg2)
    return arg1

things=[1,2,3]
print(fn1(things,4))
print(fn1(things))
print(fn1())
print(fn1())
print(fn1())

