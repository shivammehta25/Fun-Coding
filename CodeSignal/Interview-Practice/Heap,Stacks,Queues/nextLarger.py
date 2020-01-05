# https://app.codesignal.com/interview-practice/task/MdHZFgZFERPPagfdD/solutions
def nextLarger(arr):
    N = len(arr)
    max_stack = [-1, arr[N-1]]
    arr[N-1] = -1
    for i in range(2, len(arr) + 1):
        if arr[N-i] > max_stack[-1]:
            while max_stack[-1] != -1 and arr[N-i] > max_stack[-1]:
                max_stack.pop()

        temp = arr[N-i]
        arr[N-i] = max_stack[-1]
        max_stack.append(temp)

    return arr
