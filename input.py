print("Enter your name:")
x = input()
print("Hello ", x)

price = 22
txt = "The price is {:.2f} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {2} pieces of item number {1} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))