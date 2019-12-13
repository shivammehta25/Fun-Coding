# https://app.codesignal.com/challenge/Zwx3cM3w543cC3sDP


def numberOfOperations(a, b):
    count = 0
    while a and b:
        if a % b == 0:
            a //= b
        else:
            b //= a
        count += 1
        print(a, b)
    return count - 1
