def part1():
    max_calories = 0
    current_clories = 0
    with open('data.txt', 'r') as f:
        for line in f:
            if line == '\n':
                max_calories = max(max_calories, current_clories)
                current_clories = 0
            else:
                current_clories += int(line.strip())
    print(max_calories)


def part2():
    calories_list = []
    current_clories = 0
    with open('data.txt', 'r') as f:
        for line in f:
            if line == '\n':
                calories_list.append(current_clories)
                current_clories = 0
            else:
                current_clories += int(line.strip())
    print(sum(sorted(calories_list, reverse=True)[:3]))


if __name__ == "__main__":
    part1()
    part2()