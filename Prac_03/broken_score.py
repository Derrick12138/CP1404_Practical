"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# score = float(input("Enter your score: "))
#
# if score < 0 or score > 100:
#     print("sorry you enter a unavailable score")
# elif score >= 90:
#     print("you are excellent")
# elif score >= 50:
#     print("you have passed")
# else:
#     print("your score is bad")


def main():
    score = float(input("Enter your score: "))
    result = determine_grades(score)
    print("you got the " + result + " result.")

def determine_grades(score):
    if score < 0 or score > 100:
        return "unavailable score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "passed"
    else:
        return "bad"

main()