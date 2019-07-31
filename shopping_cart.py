shopping_cart = [{'name':'hat','price':10},{'name':'dress','price':30},{'name':'shirt','price':25},{'name':'glasses','price':43}]
total = 0
for item in shopping_cart:
    total += item['price']
    print(f"You item name is: {item['name']} and the price for item is: {item['price']}")
print(f"Your total is {total}")