"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



score = float(input("Enter your score: "))

if score < 0 or score > 100:
    print("sorry you enter a unavailable score")
elif score >= 90:
    print("you are excellent")
elif score >= 50:
    print("you have passed")
else:
    print("your score is bad")



# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")