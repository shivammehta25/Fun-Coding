# https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1439/


def print_string(i, string):
    if i == len(string):
        return

    print_string(i + 1, string)

    print(string[i], end='')


print_string(0, 'abcdefghijklmnopqrst')
