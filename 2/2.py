def find_possible(line: str, max_red: int, max_green: int, max_blue: int) -> int:
    """Return game id int if possible, 0 if impossible"""
    game_info, results = line.split(": ")

    for cycle in results.split("; "):
        for pair in cycle.split(", "):
            number, color = pair.split(" ")
            number = int(number)
            if color == "red":
                if number > max_red:
                    return 0
            elif color == "green":
                if number > max_green:
                    return 0
            elif color == "blue":
                if number > max_blue:
                    return 0
    return int(game_info.replace("Game ", ""))


def find_power(line: str) -> int:
    """Return game id int if possible, 0 if impossible"""
    game_info, results = line.split(": ")
    max_red, max_green, max_blue = 0, 0, 0

    for cycle in results.split("; "):
        for pair in cycle.split(", "):
            number, color = pair.split(" ")
            number = int(number)
            if color == "red":
                max_red = max(number, max_red)
            elif color == "green":
                max_green = max(number, max_green)
            elif color == "blue":
                max_blue = max(number, max_blue)
    return max_red * max_green * max_blue


def part1(fname: str):
    red, green, blue = 12, 13, 14
    with open(fname) as f:
        text = f.read().split("\n")
    total = sum([find_possible(x, red, green, blue) for x in text])
    print(total)


def part2(fname: str):
    with open(fname) as f:
        text = f.read().split("\n")
    total = sum([find_power(line) for line in text])
    print(total)


def main():
    part1("test.txt")
    part1("input.txt")
    part2("test.txt")
    part2("input.txt")


main()
