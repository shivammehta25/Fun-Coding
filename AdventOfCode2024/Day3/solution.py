import re

def load_file(path="dummy_inp.txt"):
    with open(path) as f:
        arr = f.readlines()
        
    arr = "".join(arr)
    
    return arr

def parse_mult(match):
    a, b = match.split(",")
    a = int(a.split("(")[1])
    b = int(b.split(")")[0])
    return a * b


def B(inp):
    exp = re.compile(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)')
    matches = exp.findall(inp)
    print(matches)
    activate = True
    total = 0
    for m in matches:
        if m == "do()":
            activate = True
            continue
        elif m == "don't()":
            activate = False
            continue
        
        if activate:
            total += parse_mult(m)
    
    print(total)


def A(inp):
    exp = re.compile(r'mul\([0-9]+,[0-9]+\)')
    matches = exp.findall(inp)
    
    total = 0
    for m in matches:
        total += parse_mult(m)
 
    print(total)


if __name__ == "__main__":
    inp = load_file('inp.txt')
    B(inp)
    


    