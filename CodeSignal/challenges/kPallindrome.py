# https://app.codesignal.com/challenge/Cg7JueyPBNPfycb7x
def find_value(string, i, end, k):
    if k < 0:
        return False
    if i == end:
        return True
    while string[i] == string[end]:
        i += 1
        end -= 1
        if abs(end - i) <= 1:
            return True
        
    if find_value(string, i + 1, end, k - 1):
        return True
    if find_value(string, i, end - 1, k - 1):
        return True
    
    return False

    
def kpalindrome(s, k):
    return find_value(s, 0, len(s) - 1, k)

    


