from utils import Input

def is_valid_id(id: str | int) -> bool:
    if isinstance(id, int):
        id = str(id)

    l = len(id) // 2
    if id[:l] == id[l:]:
        return False

    return True


def is_valid_id2(id: str | int) -> bool:
    if isinstance(id, int):
        id = str(id)

    L = len(id)

    for l in range(1, L//2 + 1):
        if L % l != 0:
            continue
        orig = id[:l]
        if orig * (L // l) == id:
            return False
    
    return True
         
def A():
    input = Input(2, 'a')
    INPUT = input.data
    INPUT = [x.split('-') for x in INPUT[0].split(',')]
    ans = 0
    for s, e in INPUT:
        for n in range(int(s), int(e) + 1):
            if not is_valid_id(n):
                ans += n
                # print(n)
    

    print(ans)
            
    


def B():
    input = Input(2, 'a')
    INPUT = input.data
    INPUT = [x.split('-') for x in INPUT[0].split(',')]
    ans = 0
    for s, e in INPUT:
        for n in range(int(s), int(e) + 1):
            if not is_valid_id2(n):
                ans += n
    

    print(ans)

if __name__ == '__main__':
    A()
    print("-" * 50)
    B()

    # print(is_valid_id2('12341234'))
    # print(is_valid_id2(123123123))
    # print(is_valid_id2(1188511885))
    # print(is_valid_id2(2121212118))