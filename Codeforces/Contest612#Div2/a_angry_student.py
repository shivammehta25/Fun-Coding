t = int(input())
while t:
    t -= 1
    n = int(input())
    max_ = 0
    current = 0
    a_found = False
    for i in input():
        if i == 'A':
            a_found = True
            if max_ < current:
                max_ = current
            current = 0
        else:
            if a_found:
                current += 1

    print(max(max_, current))
