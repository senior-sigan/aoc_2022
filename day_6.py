def iter_chars():
    with open('day_6.txt', 'r') as fd:
        while True:
            ch = fd.read(1)
            if ch == '\n' or ch == '':
                break
            yield ch


def count_uniq_len(n):
    frame = []
    for i, ch in enumerate(iter_chars()):
        if len(frame) == n:
            frame.pop(0)
        frame.append(ch)
        if len(set(frame)) == n:
            return i + 1
    return -1



def part_1():
    print(count_uniq_len(4))

def part_2():
    print(count_uniq_len(14))

part_1()
part_2()