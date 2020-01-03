# https://app.codesignal.com/interview-practice/task/aRwxhGcmvhf6vKPCp
from collections import deque


def simplifyPath(path):
    path = path.split('/')
    stack = deque()
    for i, value in enumerate(path):
        if value == '':  # and ( i == 0 or i == (len(path) - 1)):
            continue
        elif value == '.':
            continue
        elif value == '..':
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(value)

    return '/' + '/'.join(stack)
