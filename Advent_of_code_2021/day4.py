from pprint import pformat


class Board:
    def __init__(self, lines):
        self.data = []
        self.dict = {}
        for i, line in enumerate(lines):
            current_row = []
            for j, element in enumerate(line.split()):
                current_row.append([int(element), 0])
                self.dict[int(element)] = (i, j)
            self.data.append(current_row)

        assert len(
            self.dict) == 25, f"Invalid bingo board, should be 25 elements found {len(self.dict)}"
        assert (len(self.data) == 5) and len(
            self.data[0]) == 5, "Invalid bingo board, len mismatch check"

    def __getitem__(self, indexes):
        i, j = indexes
        return self.data[i][j]

    def __str__(self) -> str:
        return pformat(self.data)

    def mark(self, number):
        if number in self.dict:
            i, j = self.dict[number]
            self.data[i][j][1] = 1

    def _check_rows(self):
        for row in self.data:
            bingo = all([x[1] == 1 for x in row])
            if bingo:
                return True

        return False

    def _check_column(self):
        for j in range(len(self.data[0])):
            bingo = all([row[j][1] == 1 for row in self.data])
            if bingo:
                return True
        return False

    def _unmarked_sum(self):
        s = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                x, mark = self.data[i][j]
                if mark == 0:
                    s += x
        return s

    def check_bingo(self):
        bingo = self._check_rows()
        if bingo:
            return True, self._unmarked_sum()
        bingo = self._check_column()
        if bingo:
            return True, self._unmarked_sum()
        return False, 0


def open_file(file):
    with open(file) as f:
        lines = f.readlines()
        inputs = [int(x) for x in lines[0].split(',')]
        boards = []
        i = 2
        while i < len(lines):
            boards.append(Board(lines[i: i + 5]))
            i += 6

    return inputs, boards


def day4_a(inputs, boards):
    for inp in inputs:
        if inp == 24:
            print(1)
        for board in boards:
            board.mark(inp)
            bingo, unm_sum = board.check_bingo()
            if bingo:
                print(inp, unm_sum)
                print(unm_sum * inp)
                exit()


if __name__ == '__main__':
    inputs, boards = open_file('inputs/day4.txt')
    day4_a(inputs, boards)
