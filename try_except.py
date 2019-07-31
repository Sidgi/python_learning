try:
    print(x)
except NameError:
    print('sorry bro x is not defined')
except:
    print('sorry x is not your pupik')



try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")    


try:
    print(x)
except:
    print('Something went wrong')
finally:
    print('The try exept block finished')

try:
    f = open("demofile.txt")
    f.write("Lorum ipsum")
except:
    print('Something went wrong')
finally:
    f.close()

