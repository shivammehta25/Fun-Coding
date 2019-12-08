# https://app.codesignal.com/challenge/LrAwpTnYZR6NMCbfs
# The Concept behind the algorithm was 

def maxSubarray(inputArray):
    # Kadence algorithm
    # We use two pointers, max_current and max_
    
    max_current = 0 # 
    max_ = 0 #
    start_pointer, end_pointer = 0, 0
    for index, i in enumerate(inputArray): # -2
        max_current += i # 5
        if max_current < 0:
            max_current = 0 
            start_pointer = index + 1
        else:
            if max_ > max_current:
                continue
            else:
                max_ = max_current
                end_pointer = index

    
    print(start_pointer, end_pointer)
    return max_



#------------------------------------------------
# If no pointer is required one way to rewrite the code can be
def maxSubarray(inputArray):
    max_sum = 0
    current_sum = 0
    for i in range(len(inputArray)):
        current_sum = max(0, current_sum+ inputArray[i])
        max_sum = max(current_sum, max_sum)
    
    return max_sum
