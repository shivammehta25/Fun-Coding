# https://app.codesignal.com/interview-practice/task/5A8jwLGcEpTPyyjTB/solutions
# vector can be transposed with those loops

def rotateImage(a):
    a = list(reversed(a))
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a
