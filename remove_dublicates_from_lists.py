list = [1,5,3,6,49,1]

list.sort()

length = len(list)
print(list,length)
i=0
while i<length-1:
    if i+1 < length-1:
        if list[i] == list[i+1]:
            del list[i]
    i+=1

print(list,len(list))

# second solution
array_of_numbers = [2,4,5,3,5,2,3,5]
unique_array = []
for number in array_of_numbers:
    if number not in unique_array:
        unique_array.append(number)
print(unique_array)
