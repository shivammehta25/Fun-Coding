A,B,X = map(int,input().split())
 
def can_buy(n):
    p = A*n + B*len(str(n))
    return p <= X
 
ok = 0
ng = 10**9+1
while ng-ok > 1:
    print(ng, ok)
    m = (ok+ng)//2
    print(m)
    if can_buy(m):
        ok = m
    else:
        ng = m
print(ok)
