from collections import Counter

with open("a.txt") as f:
    arr = f.readlines()
    
a, b = [], []
for item in arr:
    a_, b_ = map(int, item.split())
    a.append(a_)
    b.append(b_)
    
def A():
    a.sort()
    b.sort()

    dist = 0
    for a1, b1 in zip(a, b):
        dist += abs(a1 - b1)
        
    print(dist)
        

def B():
    with open("a.txt") as f:
        arr = f.readlines()
    
    a, b = [], []
    for item in arr:
        a_, b_ = map(int, item.split())
        a.append(a_)
        b.append(b_)
        
    b = Counter(b)
    total = 0
    for a_ in a:
        if a_ in b:
            total += a_ * b[a_]
            
    
    print(total)
    
    
    
    
if __name__ == "__main__":
    B()