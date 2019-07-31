# simple car game
command = ''
stopped = False
started = False
while command != 'quit':
    command = input('> ').lower()
    if command =='start':
        if started:
            print('Car is already started...')
        else:
            print('Car is started...') 
        started = True
    elif command == 'help':
        print(' start - to start \n stop  - to stop the car \n quit  - to exit')
    elif command == 'quit':
        print('Exiting program...')
        break
    elif command == 'stop':
        if stopped:
            print('Car is already stopped...')
        else:
            print('Car is stopped...')
            stopped = True
        started = False
    else:
        print("I don't know this command")