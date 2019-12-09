# https://app.codesignal.com/challenge/rcTSmoy6pRx7frN4y
def uniqueDigitProducts(a):
    unique_values = set()
    for digit in a:
        product = 1
        for i in str(digit): 
            product*=int(i)
        unique_values.add(product)
    return len(unique_values)
