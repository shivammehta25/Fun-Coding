# https://app.codesignal.com/interview-practice/task/oJXTWuwEZiC6FTw3A
cache = {}
def climbingStairs(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    else:
        if n in cache:
            return cache[n]
        else:
            value = climbingStairs(n-1) + climbingStairs(n-2)
            cache[n] = value
            return value
