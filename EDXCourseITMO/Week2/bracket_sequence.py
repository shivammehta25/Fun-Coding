

out = open('output.txt', 'w')
with open('input.txt', 'r') as input:
    n = int(input.readline())
    for line in input:
        stack = []
        line = line.strip()
        for char in line:
            if not stack:
                stack.append(char)
                if char == ')' or char == ']':
                    break
                continue

            if (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '['):
                break
            elif (char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '['):
                stack.pop()
                continue

            stack.append(char)
        print(stack)
        if not stack:
            out.writelines('YES\n')
        else:
            out.write('NO\n')

out.close()
