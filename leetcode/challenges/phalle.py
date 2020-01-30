s = 'aeiaaiooaa'
vovels = 'aeiou'
i = 0
s_i = 0
count = 0
while s_i < len(s) and i < len(vovels):
    if s[s_i] == vovels[i]:
        count += 1
    if ord(s[s_i]) > ord(vovels[i]):
        i += 1
        continue

    s_i += 1
    

print(count if i == (len(vovels) - 1) else 0)
