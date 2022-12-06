'''
https://adventofcode.com/2022/day/3

На самом деле задача про сортировку подсчетом
'''

N = ord('z') - ord('A')

def pos(ch):
    return ord(ch) - ord('A')

def priority(ch):
    if ord(ch) < ord('a'):
        return ord(ch) - ord('A') + 27
    else:
        return ord(ch) - ord('a') + 1
    


def parse():
    with open('day_3.txt') as fd:
        while True:
            line = fd.readline().strip()
            if line == '':
                break
            middle = len(line) // 2
            yield line[:middle], line[middle:]

def find_bad_item(left, right):
    counter = [0] * (N+1)
    for ch in left:
        counter[pos(ch)] = 1
    for ch in right:
        if counter[pos(ch)] == 1:
            return priority(ch)
    return 0

def part_1():
    s = 0
    for left, right in parse():
        s += find_bad_item(left, right)
    print(s)

def parse2():
    with open('day_3.txt') as fd:
        while True:
            line = fd.readline().strip()
            if line == '':
                break
            yield [line, fd.readline().strip(), fd.readline().strip()]

def find_common(arr):
    i = set.intersection(*[set(el) for el in arr])
    common = list(i)[0]
    return priority(common)

def part_2():
    s = 0
    for group in parse2():
        s += find_common(group)
    print(s)

part_2()