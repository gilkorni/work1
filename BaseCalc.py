def Dec_To_Hex(num):
    Hex = ""
    while num > 0:
        whole = num // 16
        remainder = num % 16
        Hex = ''.join((number_to_letter(remainder), Hex))
        num = whole
    return Hex
def hex_to_dec(num):
    count = len(num) - 1
    hexnum = 0
    for letter in num:
        hexnum += int(letter_to_number(letter)) * (16**count)
        count -= 1
    print(hexnum)

def number_to_letter(number):
    if number == 10:
        return "A"
    elif number == 11:
        return 'B'
    elif number == 12:
        return 'C'
    elif number == 13:
        return 'D'
    elif number == 14:
        return 'E'
    elif number == 15:
        return 'F'
    else:
        return str(number)

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

print(Dec_To_Hex(758285))