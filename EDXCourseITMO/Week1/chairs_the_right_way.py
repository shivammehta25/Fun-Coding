# https://stackoverflow.com/a/40254850/9384082

if __name__ == '__main__':
    with open('input.txt', 'r') as inp:
        a = list(map(int, inp.readline().split()))

    with open('output.txt', 'w') as out:
        out.write(str(sum(a)/6))
        out.write('\n')
