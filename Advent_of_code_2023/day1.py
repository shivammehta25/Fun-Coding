from helpers import read_file

# data = read_file("inputs/day1_test.txt")
data = read_file("inputs/day1_a.txt")

def A():
    total = 0
    for line in data:
        first, last = None, None
        for char in line:
            if char.isnumeric():
                first = char
                break
        for char in reversed(line):
            if char.isnumeric():
                last = char
                break
        total += int(first + last)


    print(total)
    
    
def B():
    digits = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    # Now we also need to check for the word if the digit exists we need to add it to the total
    total = 0
    for line in data:
        first, last = None, None
        ptr = 0
        while ptr < len(line):
            if line[ptr].isnumeric():
                first = line[ptr]
                break
            for j, digit in enumerate(digits):
                if digit == line[ptr:ptr+len(digit)]:
                    first = str(j+1)
                    break
            if first is not None:
                break
            
            ptr+=1

        ptr = len(line)
        while ptr >= 0:
            if ptr < len(line) and line[ptr].isnumeric():
                last = line[ptr]
                break
            for j, digit in enumerate(digits):
                if digit == line[ptr-len(digit):ptr]:
                    last = str(j+1)
                    break
            if last is not None:
                break

            ptr-=1
        total += int(first + last) 

    print(total)


if __name__ == "__main__": 
    B()