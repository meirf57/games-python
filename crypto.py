# Code Message

print('Project -  Crypto')

key = 'abcdefghijklmnopqrstuvwxyz !'
value = 'qwertyuiopasdfghjklzxcv ?bnm'


def ninja():
    dict_e = dict(zip(key, value))
    dict_d = dict(zip(value, key))

    msg = input('What is the message: ')
    mode = input('Type (e) to encode (d) to decode: ')

    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])

    return new_msg.capitalize()


print(ninja())
