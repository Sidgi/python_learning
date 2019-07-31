price = 100000
downpayment = 0
credit_score_is_good = True
if credit_score_is_good:
    downpayment = price * 0.1
else: 
    downpayment = price * 0.2

print(f'Your downpayment is ${int(downpayment)}')

name = input('Enter your name: ')
if len(name)<3:
    print('Name cannot be less than 3 chars')
    name = input('Enter your name again')
elif len(name)>20:
    print('Name cannot be more than 50 chars')
    name = input('Reenter your name')
elif len(name)>3 and len(name)< 20:
    print('Thank you. Name looks good')