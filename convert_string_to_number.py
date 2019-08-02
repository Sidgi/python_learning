
number_dictionary = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9
}
array_of_numbers = []
def convertion(numbers):
    for number in numbers:
        for item in number_dictionary:
            if item == number:
                array_of_numbers.append(number_dictionary[item])
    coefficient = len(array_of_numbers) -1
    index = 0
    result = 0
    while index <= coefficient:
        result +=array_of_numbers[index]*10**(coefficient-index)
        index+=1
    print(result,type(result))
    return result


convertion('453453453')