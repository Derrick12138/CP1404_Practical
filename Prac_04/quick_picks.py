import random


def main():
    for i in range(6):
        list = []
        for j in range(5):
            number = random.randint(1, 45)
            while number in list:
                number = random.randint(1, 45)
            list.append(number)
        list.sort()
        print(" ".join("{:2}".format(number) for number in list))
main()