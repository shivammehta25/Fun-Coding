# https://app.codesignal.com/challenge/BQbA4BNhAmN4Xc9NL?solutionId=qwPm4KbEBZ5ExiD9T
def reverseToSort(inputArray):
    n_reversed = False
    start_n = None
    pre_n = None
    for i in range(1, len(inputArray)):

        if inputArray[i-1] == inputArray[i] or inputArray[i] == pre_n:
            return False
        if start_n:
            if inputArray[i-1] < inputArray[i]:
                n_reversed = True
                if inputArray[i] <= start_n:
                    return False
                if pre_n:
                    if inputArray[i-1] <= pre_n:
                        return False
                start_n = None
        else:
            if inputArray[i-1] > inputArray[i]:
                if n_reversed:
                    return False
                start_n = inputArray[i-1]
                if i >= 2:
                    pre_n = inputArray[i-2]
                    if inputArray[i] <= pre_n:
                        return False
                else:
                    None

    return True
