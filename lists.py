new_list = ['John','Mary','Henry','Jerry','Frank']

# Change Henry to Holly
new_list[2] = 'Holly'

for name in new_list:
    print(name)

numbers = [3,5,19,62,33,43]

biggest_number = -1
length = len(numbers)
for i in range(length):
    if numbers[i]>biggest_number:
        biggest_number = numbers[i]
    
print(biggest_number)
    