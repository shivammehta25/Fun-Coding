# https://app.codesignal.com/challenge/rbwtuZjSG8zJQszCz
def twoArraysNthElement(array1, array2, n):
    len1 = len(array1)
    len2 = len(array2)
    i = 0
    j = 0
    counter = 0
    while i < len1 and j < len2:
        if array1[i] < array2[j]:
            current_number = array1[i]
            i += 1
        else:
            current_number = array2[j]
            j += 1
        if counter == n:
            return current_number

        counter += 1

    while i < len1:
        current_number = array1[i]
        i += 1
        if counter == n:
            return current_number
        counter += 1

    while j < len2:
        current_number = array2[j]
        j += 1

        if counter == n:
            return current_number
        counter += 1
