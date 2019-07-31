# while loop executes statement as long as condition is true

i = 1 

while i<6:
    print(i)
    i+=1

# Break statement stops loop even if the condition still true

i = 1 

while  i<6:
    print(i)
    if i == 3:
        break
    i+=1


# Continue statement continues loop
i = 1
while i<6:
    i+=1
    if i==3:
        continue
    print(i)