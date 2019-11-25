n = int(input())
a = input()
for c in a:
    next_char = (65 + (ord(c) + n) % 91) if (ord(c) + n) >= 91 else (ord(c) + n)
    print(chr(next_char), end='')
