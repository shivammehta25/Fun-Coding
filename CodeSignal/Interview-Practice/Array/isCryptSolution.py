# https://app.codesignal.com/interview-practice/task/yM4uWYeQTHzYewW9H

def isCryptSolution(crypt, solution):
    crypt_dict = { v[0]: v[1] for v in solution}
    word_1 = ''.join(crypt_dict[i] for i in crypt[0])
    word_2 = ''.join(crypt_dict[i] for i in crypt[1])
    word_3 = ''.join(crypt_dict[i] for i in crypt[2])
    if (word_1.startswith('0') or word_2.startswith('0') or ( word_3.startswith('0'))) and  word_3 != '0' :
        return False
    print('{} {} {}'.format(word_1, word_2, word_3))
    return int(word_1) + int(word_2) == int(word_3)
