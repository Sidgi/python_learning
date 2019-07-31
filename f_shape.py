numbers = [5,2,5,2,2]

#for number in numbers:
#    print('x'*number)


# different solution of the task
x = ''
for number in numbers:
    while number>0:
        x+='x'
        number-=1
        if number == 0:
            print(x)
            x = ''



# third solution with range function

for item in numbers:
    result = ''
    for n in range(item):
        result +='*'
    print(result)