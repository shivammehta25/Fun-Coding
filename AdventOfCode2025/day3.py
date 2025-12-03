from utils import Input


def max_argmax(nums: list[int]) -> tuple[int, int]:
    val, idx = -1, -1
    for i, n in enumerate(nums):
        if n > val:
            val = n
            idx = i

    return val, idx


def max_val_char(nums: list[int], n: int) -> int:
    if n == 0:
        return 0
    slice_idx = -(n - 1) if n > 1 else None
    c, idx = max_argmax(nums[:slice_idx])
    return c * (10 ** (n - 1))  + max_val_char(nums[idx+1:], n-1)


def A():
    input = Input(3, 'a').convert_to_2d(to_int=True)
    INPUT = input.data

    ans = 0
    for bank in INPUT:
        c1, idx = max_argmax(bank[:-1])
        c2, _ = max_argmax(bank[idx + 1:])
        ans += c1 * 10 + c2

    
    print(ans)


def B():

    input = Input(3, 'a').convert_to_2d(to_int=True)
    INPUT = input.data

    ans = 0
    for bank in INPUT:
        a = int(max_val_char(bank, 12))
        ans += a

    print(ans)


if __name__ == '__main__':
    A()
    print("-" * 50)
    B()
