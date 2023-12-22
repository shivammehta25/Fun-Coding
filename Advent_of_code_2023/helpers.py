def read_file(file_loc):
    lines = []
    with open(file_loc, "r") as f:
        for line in f:
            lines.append(line.strip())
    return lines