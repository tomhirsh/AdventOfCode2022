import pdb

def char_score(char):
    if ord(char) >= ord('a'): # lower case
        return ord(char) - ord('a') + 1

    return ord(char) - ord('A') + 27


def part1():
    score = 0
    with open('data.txt', 'r') as f:
        for line in f:
            line_stripped = line.strip()
            half_line = int(len(line_stripped)/2)
            first_half = line_stripped[:half_line]
            second_half = line_stripped[half_line:]
            char_in_both_halves = set(first_half).intersection(second_half).pop()
            score += char_score(char_in_both_halves)

    print(score)


def part2():
    score = 0
    group_sets = []
    with open('data.txt', 'r') as f:
        for i, line in enumerate(f):
            group_sets.append(set(line.strip()))
            if (i+1) % 3 == 0 and i > 1:
                common_char = (group_sets[0] & group_sets[1] & group_sets[2]).pop()
                score += char_score(common_char)
                group_sets = []

    print(score)

if __name__ == "__main__":
    part1()
    part2()