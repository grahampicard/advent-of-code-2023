def parse_map_file(line):
    if line[:5] == "seeds":
        key, values = line.split(": ")
        values = [int(x) for x in values.split(" ")]
        return key, values
    else:
        key, values = line.split(":\n")
        values = [[int(y) for y in x.split(" ")] for x in values.split("\n")]
        return key, values


def src_dst_map(remappings):
    current_map = {x: x for x in range(100)}
    for vals in remappings:
        dst, src, num = vals
        for val in range(num):
            current_map[src + val] = dst + val
    return current_map


def part1(fname):
    with open(fname, "r") as f:
        data = f.read()
    data = data.split("\n\n")
    mappings = {k: v for (k, v) in [parse_map_file(x) for x in data]}
    order = tuple(mappings.keys())

    # for i, (k, v) in enumerate(mappings):
    # if 'map' in k:


def main():
    part1("test.txt")


main()
