# https://app.codesignal.com/challenge/4nwZHgbjAXTquopxR
def triangleExistence(sides):
    a, b, c = map(int, sides)
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True
