# https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q/description

import math
def firstDuplicate(a):
    element_dict = {}
    min_value = math.inf
    for i, e in enumerate(a):
        if e in element_dict:
            return e
        else:
            element_dict[e] = i+1
    return -1
