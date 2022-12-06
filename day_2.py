# https://adventofcode.com/2022/day/2

costs = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

score_table = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3},
}

solution_table = {
    'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
    'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
    'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'},
}

def parse():
    with open('day_2.txt', 'r') as fd:
        while True:
            line = fd.readline()
            if line == '':
                break
            a,b = line.strip().split(' ')
            yield a, b


def part_1():
    score = 0
    for a, b in parse():
        score +=  costs[b] + score_table[a][b]
    print(score)

def part_2():
    score = 0
    for a, b in parse():
        bb = solution_table[a][b]
        score += costs[bb] + score_table[a][bb]
    print(score)

# part_1()
part_2()