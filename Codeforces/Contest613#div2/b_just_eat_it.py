from math import inf
t = int(input())
while t:
    t -= 1

    n = int(input())
    a = list(map(int, input().split()))

    # max_sum = -inf
    # current_sum = 0
    # i = 0
    # for x in a:
    #     current_sum += x
    #     if current_sum > max_sum:
    #         max_sum = current_sum
    #         i += 1
    #     if current_sum < 0:
    #         current_sum = 0

    # print(max_sum, sum(a))

    # if max_sum > sum(a) or i != len(a):
    #     print('NO')
    # else:
    #     print('YES')

    def check(a):
        s = 0
        for i in a:
            s += i
            if s <= 0:
                return False
        s = 0
        for i in a[::-1]:
            s += i
            if s <= 0:
                return False

        return True

    if check(a):
        print('YES')
    else:
        print('NO')
