# https://app.codesignal.com/challenge/RLmESwd834Bjejc3x
def visitsOnCircularRoad(n, visitsOrder):
    sum = 0
    N = len(visitsOrder)
    current = 1
    for i in range(len(visitsOrder)):
        sum += min(abs(current - visitsOrder[i]), n - abs( current - visitsOrder[i])  )
        current = visitsOrder[i]
    
    return sum
