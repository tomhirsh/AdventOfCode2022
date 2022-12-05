from collections import defaultdict


def part1():
    crates = defaultdict(list)
    with open('data.txt', 'r') as f:
        for line in f:
            if '[' in line:
                for i in range(int(len(line) / 4)):
                    c = line[1+4*i]
                    if c != ' ':
                        crates[i].append(c)

            elif 'move' in line:
                com = line.strip().split(' ')
                for _ in range(int(com[1])):
                    crates[int(com[-1])-1].append(crates[int(com[3])-1].pop())

            elif line!= '\n':
                for val in crates.values():
                    val.reverse()

    print(''.join([crates[i][-1] for i in range(len(crates))]))


def part2():
    crates = defaultdict(list)
    with open('data.txt', 'r') as f:
        for line in f:
            if '[' in line:
                for i in range(int(len(line) / 4)):
                    c = line[1+4*i]
                    if c != ' ':
                        crates[i].append(c)

            elif 'move' in line:
                com = line.strip().split(' ')
                crates_to_move = crates[int(com[3])-1][-int(com[1]):]
                crates[int(com[3])-1] = crates[int(com[3])-1][:-int(com[1])]
                crates[int(com[-1])-1].extend(crates_to_move)

            elif line != '\n':
                for val in crates.values():
                    val.reverse()

    print(''.join([crates[i][-1] for i in range(len(crates))]))


if __name__ == "__main__":
    part1()
    part2()