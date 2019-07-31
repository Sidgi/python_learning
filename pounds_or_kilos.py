difference = 0.45
weight = input('Enter your weight: ')
type = input('(L)bs or (K)g: ')
converted = type.lower()
if converted == 'l':
    print(f'Your weight is {float(weight)*difference}')
elif converted == 'k':
    print(f'Your weight is {float(weight)/difference}')
else:
    'Please enter l for lbs or k for kg'