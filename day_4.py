def parse():
    with open('day_4.txt', 'r') as fd:
        while True:
            line = fd.readline().strip()
            if line == '':
                break
            l1, l2 = line.split(',')
            l1p = l1.split('-')
            l2p = l2.split('-')
            yield {
                'l': int(l1p[0]),
                'r': int(l1p[1]),
            }, {
                'l': int(l2p[0]),
                'r': int(l2p[1]),
            }

def contains_full(a, b):
    return (a['l'] <= b['l'] and a['r'] >= b['r']) or \
        (b['l'] <= a['l'] and b['r'] >= a['r'])

def part_1():
    counter = 0
    for a, b in parse():
        if contains_full(a, b):
            counter += 1
    return counter

def part_2():
    pass

print(part_1())