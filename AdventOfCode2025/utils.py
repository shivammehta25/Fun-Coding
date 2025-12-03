import os

def load_file(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def row_to_2d(nums: list[str], to_int: bool) -> list[list[str | int]]:
    return [[int(x) if to_int else x for x in row] for row in nums]

class Input:
    def __init__(self, day: int, puzzle_part: str):
        self.day = day
        self.puzzle_part = puzzle_part
        self.sample = load_file(f"inputs/day{day}/sample_{puzzle_part}.txt")
        self.data = load_file(f"inputs/day{day}/{puzzle_part}.txt")
        self.tests = {i: load_file(f"inputs/day{day}/test_{i}.txt") if os.path.exists(f"inputs/day{day}/test_{i}.txt") else None for i in range(1, 10)}

    

    def convert_to_2d(self, to_int: bool = False):
        self.sample = row_to_2d(self.sample, to_int)  # type: ignore[arg-type]
        self.data = row_to_2d(self.data, to_int)  # type: ignore[arg-type]
        self.tests = {i: row_to_2d(val, to_int) if val is not None else None for i, val in self.tests.items()}  # type: ignore[arg-type]
        return self