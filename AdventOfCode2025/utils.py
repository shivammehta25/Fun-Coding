import os

def load_file(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]



class Input:
    def __init__(self, day: int, puzzle_part: str):
        self.day = day
        self.puzzle_part = puzzle_part
        self.sample = load_file(f"inputs/day{day}/sample_{puzzle_part}.txt")
        self.data = load_file(f"inputs/day{day}/{puzzle_part}.txt")
        self.tests = {i: load_file(f"inputs/day{day}/test_{i}.txt") if os.path.exists(f"inputs/day{day}/test_{i}.txt") else None for i in range(1, 10)}