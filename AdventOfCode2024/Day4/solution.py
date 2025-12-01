from pprint import pprint

def convolve_count(inp, kernel, ans):
    r = len(kernel) 
    c = len(kernel[0])
    
    m = len(inp)
    n = len(inp[0])
    count = 0
    for i in range(m - r + 1):
        for j in range(n - c + 1):
            matched = 1
            for k in range(r):
                if matched == 0:
                    break
                
                for l in range(c):
                    if kernel[k][l] != "." and inp[i + k][j + l] != kernel[k][l]:
                        matched = 0
                        break
            


            if matched:
                for k in range(r):
                    for l in range(c):
                        if kernel[k][l] != ".":
                            ans[i+k][j+l] = kernel[k][l]
                
            
            count += matched 

    return count
    


def load_file(path="dummy_inp.txt"):
    with open(path) as f:
        arr = f.readlines()
    
    arr = [[x for x in row.strip()] for row in arr]
    
    return arr

horizontal = [["X", "M", "A", "S"]]
horizontal_backwards = [["S", "A", "M", "X"]]
vertical = [["X"], ["M"], ["A"], ["S"]]
vertical_backwards = [["S"], ["A"], ["M"], ["X"]]
diag1 = [["X", ".", ".", "."], [".", "M", ".", "."], [".", ".", "A", "."], [".", ".", ".", "S"]]
diag2 = [[".", ".", ".", "X"], [".", ".", "M", "."], [".", "A", ".", "."], ["S", ".", ".", "."]] 
rev_diag1 = [["S", ".", ".", "."], [".", "A", ".", "."], [".", ".", "M", "."], [".", ".", ".", "X"]]
rev_diag2 = [[".", ".", ".", "S"], [".", ".", "A", "."], [".", "M", ".", "."], ["X", ".", ".", "."]]


mas_kernel1 = [["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]]
mas_kernel2 = [["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]]
mas_kernel3 = [["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]]
mas_kernel4 = [["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]]

all_kernels = [
    horizontal,
    horizontal_backwards,
    vertical,
    vertical_backwards ,
    diag1,
    diag2,
    rev_diag1,
    rev_diag2
]

mas_kernels = [
    mas_kernel1,
    mas_kernel2,
    mas_kernel3,
    mas_kernel4
]

def A(inp):
    count = 0

    m = len(inp)
    n = len(inp[0])
    ans = [["."] * n for _ in range(m)]

    for kernel in all_kernels:
        count += convolve_count(inp, kernel, ans)
    
    pprint(["".join(x) for x in ans])
    print(count)

def B(inp):
    m = len(inp)
    n = len(inp[0])
    ans = [["."] * n for _ in range(m)]
    count = 0
    for mas_kernel in mas_kernels:
        count += convolve_count(inp, mas_kernel, ans)
    
    pprint(["".join(x) for x in ans])
    print(count)


if __name__ == "__main__":
    inp = load_file('dummy_inp.txt')
    A(inp)
    

