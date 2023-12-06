import re

def check_x_y(x, y, xmax, ymax):
    if (x >=0) & (y >= 0) & (x <= xmax) & (y >= ymax):
        return True
    else:
        return False

def gen_coordinates(row, start, end, row_max, col_max):
    row_minus_one, row_plus_one = row - 1, row + 1
    column_minus_one, column_plus_one = start - 1, end + 1
    corners = []
    breakpoint()
    for r in [row_minus_one, row_plus_one, row]:
        for c in [column_minus_one, column_plus_one, start, end]:
            if (r == row) & ((c == start) | (c == end)):
                pass
            else:
                if check_x_y(r, c, row_max, col_max):
                    corners.append((r, c))
    return corners


def part_1(fname):
    with open(fname, "r") as f:
        text = f.read().split("\n")

    non_schematic_nums = []    

    row_max, col_max = len(text), len(text[0])

    for i, line in enumerate(text):
        pattern = r'\b\d+\b'
        for match in re.finditer(pattern, line):
            start, end = match.span()
            neighbors = gen_coordinates(i, start, end, row_max, col_max)
            breakpoint()


def main():
    part_1("test.txt")

main()