def sections_overlap_part1(section1, section2):
    return len(set(range(section2[0], section2[1]+1)) & set(range(section1[0], section1[1]+1))) > \
            min(section2[1]-section2[0], section1[1]-section1[0])

def sections_overlap_part2(section1, section2):
    return len(set(range(section2[0], section2[1]+1)) & set(range(section1[0], section1[1]+1))) >0

get_section = lambda x: [int(y) for y in x.split('-')]
counter_part1 = 0
counter_part2 = 0
with open('data.txt', 'r') as f:
    for line in f:
        elf1, elf2 = line.strip().split(',')
        if sections_overlap_part1(get_section(elf1), get_section(elf2)):
            counter_part1 += 1
        if sections_overlap_part2(get_section(elf1), get_section(elf2)):
            counter_part2 += 1

print(counter_part1)
print(counter_part2)