# itoc = {0: ‘a’, 1:’b’, 2:’c’}
# ctoi = {‘a’: 0, ‘b’: 1, ’c’:2}
# current_element = ‘?’
# j = 0
# for i, element in enumerate(l):
# 	if l[i] == ‘?’:
# 		if current_element= ‘?’:
# 			current_element = 0
# 		else:
# 			current_element = (current_element + 1) % 3
# 			if  i < n -1 and current_element == arr[i+1]:
# 				current_element = (current_element + 1) % 3
# 		l[i] = itoc[current_element]
# 	else:
# 		i_element = ctoi[l[i]]
# 		if i_element == current_element:
# 			return -1
# 		current_element = i_element

def check_beauty(arr):
    itoc = {0: 'a', 1: 'b', 2: 'c'}
    ctoi = {'a': 0, 'b': 1, 'c': 2}
    arr = [i for i in arr]
    n = len(arr)
 #   print(f'Start {arr}')
    current_element = '?'
    for i, element in enumerate(arr):
        if arr[i] == '?':
            if current_element == '?':
                current_element = 0
            else:
                current_element = (current_element + 1) % 3
            if i<= n-2 and arr[i+1] != '?' and current_element == ctoi[arr[i+1]]:
#               print('Itthe aa')
                current_element = (current_element + 1) % 3
            arr[i] = itoc[current_element]
#            print(f'Mai paaya: {arr[i]}')
        else:
            i_element = ctoi[arr[i]]
#            print(f'Aae milya : {i_element}')
            if i_element == current_element:
                return -1
            current_element = i_element
#        print(current_element)  
    return ''.join(arr)

n = int(input())
for _ in range(n):
    print(check_beauty(input()))

