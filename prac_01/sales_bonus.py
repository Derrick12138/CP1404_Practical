"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


print("please enter youe sales and calcuate the bonus, press the number under 0 the end the programming")

sales = float(input("Please Enter the sales ：$"))
while sales > 0:
    if sales < 1000:
        bonus = sales * 0.1
        print("Congratulation, you have got 10% bonus {:.2f}".format(bonus))
    else:
        bonus = sales * 0.15
        print("Congratulation, you have got 15% bonus {:.2f}".format(bonus))
    sales = float(input("Please Enter the sales ：$"))
print("thank u and bye")