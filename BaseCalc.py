def hex_to_dec(num):
    count = len(num) - 1
    hexnum = 0
    for letter in num:
        hexnum += int(letter_to_number(letter)) * (16**count)
        count -= 1
    print(hexnum)

def letter_to_number(letter):
    if letter == 'a' or letter == 'A':
        return 10
    elif letter == 'b' or letter == 'B':
        return 11
    elif letter == 'c' or letter == 'C':
        return 12
    elif letter == 'd' or letter == 'D':
        return 13
    elif letter == 'e' or letter == 'E':
        return 14
    elif letter == 'f' or letter == 'F':
        return 15
    else:
        return letter



hex_to_dec("5ec")

