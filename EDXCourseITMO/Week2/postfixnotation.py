def postfix_calculator(arr):
    s = []
    for element in arr:
        if element.isnumeric():
            s.append(int(element))
        else:
            x = s.pop()
            y = s.pop()
            if element == '+':
                value = x + y
            elif element == '-':
                value = y - x
            elif element == '*':
                value = x * y
            else:
                value = x // y

            s.append(value)
    if len(s) == 1:
        return s.pop()


o = open('output.txt', 'w')
with open('input.txt') as inp:
    n = inp.readline()
    arr = inp.readline().strip().split()
    o.write(str(postfix_calculator(arr)) + '\n')

o.close()
