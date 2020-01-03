# https://app.codesignal.com/interview-practice/task/dYCH8sdnxGf5aGkez/solutions
def decodeString(string):
    final_output = []
    for c in string:
        if c != ']':
            final_output.append(c)
        else:
            s = []
            while(final_output[-1] != '['):
                s.append(final_output.pop())
            pop_bracket = final_output.pop()
            number = []
            while final_output and final_output[-1].isnumeric():
                number.append(final_output.pop())
            final_output.append(
                int(''.join(reversed(number))) * ''.join(reversed(s)))

    return ''.join(final_output)
