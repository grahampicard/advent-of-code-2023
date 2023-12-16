import re
import string


def check_x_y(x, y, xmax, ymax):
    if (x < 0) | (y < 0) | (x >= xmax) | (y >= ymax):
        return False
    else:
        return True


def gen_coordinates(row, start, end, row_max, col_max):
    previous_row, next_row = row - 1, row + 1
    previous_col, next_col = start - 1, end + 1
    span = [(row, c) for c in range(start, end)]
    neighbors = []
    for row_value in range(previous_row, next_row + 1):
        for col_value in range(previous_col, next_col + 1):
            if check_x_y(row_value, col_value, row_max, col_max):
                coord = (row_value, col_value)
                if coord not in span:
                    neighbors.append(coord)
    return neighbors


def part_1(fname):
    with open(fname, "r") as f:
        text = f.read().split("\n")

    schematic_nums = []
    row_max, col_max = len(text), len(text[0])
    symbols = string.punctuation.replace(".", "")

    # iterate through each line
    for i, line in enumerate(text):
        # look for the numeric pattern
        pattern = r"\b\d+\b"
        # for each match, get neighbors, check if a neighbor is a symbol
        for match in re.finditer(pattern, line):
            start, end = match.span()
            neighbors = gen_coordinates(i, start, end, row_max, col_max)
            is_schematic = False
            for row, col in neighbors:
                if text[row][col] in symbols:
                    is_schematic = True
            if is_schematic:
                schematic_nums.append(int(match.group()))
    print(sum(schematic_nums))


def main():
    part_1("test.txt")


main()
