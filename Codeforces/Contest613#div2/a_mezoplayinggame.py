n = input()
commands = input()

l = 0
r = 0
for c in commands:
    if c == 'L':
        l += 1
    else:
        r += 1

print(abs(l) + abs(r) + 1)
