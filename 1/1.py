def calibrate(line: str) -> int:
    nums = []
    for letter in line:
        if letter.isnumeric():
            nums.append(letter)
    return int(nums[0] + nums[-1])


def part1(fname):
    with open(fname, "r") as f:
        text = f.read().split("\n")
    vals = [calibrate(line) for line in text]
    print(sum(vals))


def part2(fname):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open(fname, "r") as f:
        text = f.read().split("\n")

    vals = []
    for line in text:
        ints = {}
        for i, letter in enumerate(line):
            if letter.isnumeric():
                ints[i] = int(letter)
        for j, d in enumerate(digits):
            num = line.find(d)
            while num != -1:
                ints[num] = j + 1
                num = line.find(d, num + 1)
        ordered_ints = sorted(ints)
        key_tens = ordered_ints[0]
        key_ones = ordered_ints[-1]
        vals.append(ints[key_tens] * 10 + ints[key_ones])

    print(sum(vals))


def main():
    part1("test.txt")
    part1("input.txt")
    part2("test2.txt")
    part2("input.txt")


main()
