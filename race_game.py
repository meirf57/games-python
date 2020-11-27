print('Welcome!')


def in_name():
    global name
    name = input("Please type you'r name (at least 4 characters): ")
    return str(name)


attempt = 1
in_name()
while attempt < 2:
    attempt += 1
    len_n = len(name)
    if len_n < 4:
        print('Name should be longer than 3 charachters'), in_name()
    elif len_n > 10:
        print('Name should be less than 10 charachters'), in_name()
else:
    print(f'Hello {name.capitalize()}!\nLets race!')

# Racing Game
start = "Engine running.. let's go!"
stop = "Break! engine stop."
help = 'controls:\n start - Go.\n stop - Break.\n quit - Exit game.'
running = False
in_place = False
game_time = 1
game_action = 8
while True:
    action = (input('> ')).lower()
    if action == 'start':
        if running:
            print("Car is speeding!")
        else:
            running = True
            in_place = False
            print(start)
    elif action == 'stop':
        if in_place:
            print("Car is in place.")
        else:
            in_place = True
            running = False
            print(stop)
    elif action == 'help':
        print(help)
    elif action == 'quit':
        break
    else:
        print("Sorry I don't understand")
print('Great game, I hope you enjoyed!')