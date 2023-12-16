from collections import defaultdict


def score(num: int) -> int:
    if num == 0:
        return 0
    start = 1
    num -= 1
    return start * 2**num


def part1(fname: str):
    total = 0
    with open(fname, "r") as f:
        for line in f.read().split("\n"):
            excerpt = line.split(": ")[1]
            winning, numbers = excerpt.split(" | ")
            winning = set([int(x) for x in winning.split(" ") if x])
            numbers = [int(y) for y in numbers.split(" ") if y]
            n_winning = len(winning.intersection(numbers))
            total += score(n_winning)
    print(total)


def part2(fname: str):
    card_lookup = defaultdict(lambda: 0)
    with open(fname, "r") as f:
        for line in f.read().split("\n"):
            card, excerpt = line.split(": ")
            card = int(card[4:].strip())
            winning, numbers = excerpt.split(" | ")
            winning = set([int(x) for x in winning.split(" ") if x])
            numbers = [int(y) for y in numbers.split(" ") if y]
            n_winning = len(winning.intersection(numbers))
            card_lookup[card] += 1
            for _ in range(card_lookup[card]):
                for val in range(card + 1, card + n_winning + 1):
                    card_lookup[val] += 1
    print(sum(card_lookup.values()))


def main():
    part1("test.txt")
    part1("input.txt")
    part2("test.txt")
    part2("input.txt")


main()
