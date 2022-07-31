
total = 0
number = int(input("number of items : "))

while number <= 0:
    print("sorry you have to buy some item and calcuate")
    number = int(input("number of items : "))

for i in range(number):
    price = float(input("Price of items: "))
    total = total + price

if total > 100:
    total = total - total * 0.1

print("Total price for 3 items is {:.2f}".format(total))
