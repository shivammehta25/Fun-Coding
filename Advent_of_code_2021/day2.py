

def open_file(file):
    with open(file) as f:
        data = [(x.strip().split()[0], int(x.strip().split()[1]))
                for x in f.readlines()]
    return data


def get_position(data):
    hp = 0
    d = 0
    a = 0

    # Function for first part
    # def forward(x): nonlocal hp; hp += x
    # def down(x): nonlocal d; d += x
    # def up(x): nonlocal d; d -= x

    # Function for second part
    def forward(x): nonlocal hp, d; hp += x; d += x * a
    def down(x): nonlocal a; a += x
    def up(x): nonlocal a; a -= x

    for function, x in data:
        eval(function)(x)

    print(hp * d)


if __name__ == '__main__':

    data = open_file("inputs/day2.txt")

    get_position(data)
