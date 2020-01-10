

# def permutation(a):
#     n = len(a)
#     end = True
#     for i in range(n-2, -1, -1):
#         if a[i] < a[i + 1]:
#             end = False
#             break

#     if end:
#         return []

#     pivot = i

#     for i in range(n - 1, pivot, -1):
#         if a[i] > a[pivot]:
#             a[i], a[pivot] = a[pivot], a[i]
#             break
#     a[pivot + 1:] = a[:pivot:-1]
#     return a


# n = int(input())
# f = list(map(int, input().split()))
# e = list(map(int, input().split()))
# a = sorted(f)
# first = 0
# end = 0

# p = permutation(a)
# i = 0
# while p:
#     if p == f:
#         first = i
#     if p == e:
#         end = i

#     i += 1
#     p = permutation(p)

# print(abs(end-first))

# print(permutation([2, 3, 1]))


from itertools import permutations
n = int(input())
f = list(map(int, input().split()))
e = list(map(int, input().split()))
a = sorted(f)
first = 0
end = 0
for i, l in enumerate(permutations(a)):
    if list(l) == f:
        first = i
    if list(l) == e:
        end = i

print(abs(end-first))
