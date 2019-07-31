birth_year = input("Birth year: ")
age = 2019 - int(birth_year)
print('Your age is ' + str(age))


weight_pounds = input("What's your weight in pounds? ")
weight_kg = int(weight_pounds) * 0.453592
txt = 'Your weight in kg {}'
print(txt.format(weight_kg))

print(txt.upper())
print(len(txt))