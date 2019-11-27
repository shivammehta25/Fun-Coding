s = input()
start = 0
end = len(s) -1
insertions = 0
while(start < end):
    if s[start] == s[end]:
        start += 1
        end -= 1
        continue

    if 'x' == s[end]:
        insertions += 1
        end -= 1
    elif 'x' == s[start]:
        insertions += 1
        start += 1
    else:
        print(-1)
        exit(0)

print(insertions)
    
