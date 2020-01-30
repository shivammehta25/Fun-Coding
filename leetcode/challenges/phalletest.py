from random import choice


def longest_subsequence(string):
    def helper(chosen="", i=0):
        if i == len(string):
            return chosen if set("aeiou").issubset(set(chosen)) else ""

        hashable = (chosen[-1] if chosen else None, len(chosen), i)

        if hashable in memo:
            return memo[hashable]

        if not chosen:
            res = helper("a" if string[i] == "a" else chosen, i + 1)
        elif chosen[-1] == string[i]:
            res = helper(chosen + string[i], i + 1)
        elif mapping[chosen[-1]] + 1 == mapping[string[i]]:
            sub1 = helper(chosen + string[i], i + 1)
            sub2 = helper(chosen, i + 1)

            res = sub1 if len(sub1) > len(sub2) else sub2
        else:
            res = helper(chosen, i + 1)

        memo[hashable] = res
        return res

    mapping = {x: i for i, x in enumerate("aeiou")}
    memo = {}
    return helper()


if __name__ == "__main__":
    tests = [
        "aeiaaioooaauuaeiou",
        "aaauuiieeou",
        "".join(choice("aeiou") for _ in range(40)),
        "".join(choice("aeiou") for _ in range(900)),
    ]

    for string in tests:
        subsequence = longest_subsequence(string)

        print(len(subsequence))
