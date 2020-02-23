# https://app.codesignal.com/challenge/iwQwAS9Zn5v7SNj9D
def columnTitle(number):
    s = []
    while number:
        remainder = number % 26
        if remainder == 0:
            s.append('Z')
            number = number // 26 - 1
        else:
            s.append(chr(remainder - 1 + 65))
            number = number // 26
    return ''.join(s[::-1])
