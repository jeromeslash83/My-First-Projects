from data import MORSE_CODE_DEC, MORSE_CODE_ENC

def decodeMorse(morse_code):
    """TAKES AN INPUT AND DECODES THE MORSE CODE"""
    morse = (morse_code.replace('  ', 'x ').split(' '))
    decoded = ''
    for char in morse:
        if char == 'x':
            decoded += ' '
        else:
            decoded += MORSE_CODE_DEC[char]
    print(decoded)
    

def encodeMorse(morse_code):
    """TAKES AN INPUT AND ENCODES A MORSE CODE"""
    encoded = ''
    for char in morse_code:
        if char == ' ':
            encoded += ' '
        else:
            encoded += MORSE_CODE_ENC[char]
            encoded +=  ' '
    print(encoded)
    

is_on = True
while is_on:
    to_do = input('What do you want to do? (e)ncode or (d)ecode:\n').lower()

    if to_do == 'e':
        encodeMorse(input("What do you want to encode:").upper())
    elif to_do == 'd':
        decodeMorse(input("What do you want to decode:").upper())
    else:
        print('Wrong input try again.')

    turn_off = input("Do you want to do another task? Y or N:\n").upper()
    
    if turn_off == 'Y':
        pass
    else:
        is_on = False
