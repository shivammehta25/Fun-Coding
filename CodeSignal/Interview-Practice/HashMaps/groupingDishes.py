# https://app.codesignal.com/interview-practice/task/xrFgR63cw7Nch4vXo
from collections import defaultdict

def groupingDishes(dishes):
    d = defaultdict(list)
    for dish in dishes:
        for i in range(1, len(dish)):
            if dish[0] not in d[dish[i]]:
                d[dish[i]].append(dish[0])
    print(d)
    output = []
    for l in d:
        if len(d[l]) > 1:
            output.append([l] + sorted(d[l]))
    
    return sorted(output, key=lambda x: x[0])
