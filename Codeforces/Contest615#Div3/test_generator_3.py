import random
import os

with open('input.txt', 'w') as out:
    t = random.randint(1, 100)
    out.write('{}\n'.format(t))
    arr = []
    while t:
        num = random.randint(2, 10**4)
        arr.append(num)
        out.write('{}\n'.format(num))
        t -= 1


os.system('(python c_product_of_three_numbers.py < input.txt ) > output.txt')

with open('output.txt') as inp:
    i = 0
    for line in inp:
        if line.strip() == 'NO':
            i += 1
            continue
        elif line.strip() == 'YES':
            continue
        else:
            a, b, c = map(int, line.strip().split())
            if arr[i] == a*b*c:
                print('Test Passed')
                i += 1
                continue
            else:
                print(arr[i])
                print(a, b, c)
                break


#
# 8772
# 2 3 17
