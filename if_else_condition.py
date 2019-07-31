
#classic if else and elif statement 

a = 20
b = 10
c = 100
if a>10:
    print('a more than 10')
elif a>15:
    print('a less than 10')
else:
    print('a equal 10')


## short hand writing conditions if else in python

if a>10: print ('a is more than ten')

## short hand if else

print('A') if a>b else print ('B')

## if else with 3 conditions

print('A') if a>b else print('B') if a==b else print('C')

## and keyword in python

if a>b and c>a:
    print('both conditions are true')

## or keyword in python

if a>b or c<a:
    print('at least one of the conditions is true')