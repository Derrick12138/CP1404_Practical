"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


for i in range(1, 21, 2):
    print(i, end=' ')
print()


# A
for i in range(0, 101, 10):
    print(i, end=" ")
print()


# B
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# C
number = int(input("number of stars: "))
for i in range(number):
    print("*", end="")
print()

# D
number = int(input("Number of Stars: "))
for i in range(number + 1,):
    print("*" * i)
print()
