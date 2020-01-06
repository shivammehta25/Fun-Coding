# https://app.codesignal.com/challenge/ddEZp78usMvhQEu3i
def arrayConversion(inputArray):
    k = 0
    while len(inputArray) > 1:
        k += 1
        new_array = []
        if k % 2 != 0:
            for i in range(0, len(inputArray), 2):
                first_element = inputArray[i]
                second_element = inputArray[i + 1]
                new_array.append(first_element + second_element)
        else:

            for i in range(0, len(inputArray), 2):
                first_element = inputArray[i]
                second_element = inputArray[i + 1]
                new_array.append(first_element * second_element)

        inputArray = new_array
        print(inputArray)
    return inputArray[0]
