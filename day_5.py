from collections import defaultdict

def parse():
    pyramid = defaultdict(list)
    with open('day_5.txt', 'r') as fd:
        while True:
            line = fd.readline()[:-1]
            if line == '':
                break
            for i in range(0, len(line), 4):
                if line[i] == '[':
                    pyramid[i // 4 + 1].append(line[i+1])
    
        commands = []
        while True:
            line = fd.readline().strip()
            if line == '':
                break
            parts = line.split(' ')
            commands.append((int(parts[1]), int(parts[3]), int(parts[5])))
    
    for k in pyramid:
        pyramid[k].reverse()
    
    return pyramid, commands


def part_1():
    pyramid, commands = parse()
    for cnt, src, dst in commands:
        for _ in range(cnt):
            el = pyramid[src].pop()
            pyramid[dst].append(el)

    tops = [''] * len(pyramid)
    for k in pyramid:
        tops[k-1] = pyramid[k][-1]
    print("".join(tops))

def part_2():
    pyramid, commands = parse()
    for cnt, src, dst in commands:
        buffer = []
        for _ in range(cnt):
            el = pyramid[src].pop()
            buffer.append(el)
        for _ in range(cnt):
            el = buffer.pop()
            pyramid[dst].append(el)

    tops = [''] * len(pyramid)
    for k in pyramid:
        tops[k-1] = pyramid[k][-1]
    print("".join(tops))

part_1()
part_2()