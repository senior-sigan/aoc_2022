# https://adventofcode.com/2022/day/1

# Part 1
def part_1():
    with open('day_1.txt', 'r') as fd:
        lines = fd.read().splitlines()

    m = -1
    cur = 0
    for line in lines:
        if line == '':
            if cur > m:
                m = cur
            cur = 0
        else:
            cur += int(line)

    print(m)


def partition(arr, first, last):
    pivot = arr[(first + last) // 2]
    i = first
    j = last

    while i < j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    return j


def part_sort(arr, k):
    first = 0
    last = len(arr)
    while True:
        mid = partition(arr, first, last - 1)
        if k == mid:
            return
        if k < mid:
            last = mid
        else:
            first = mid + 1


def part_2():
    '''
    Надо найти первые k-самых больших числа в массиве.
    Похоже на k-ую порядковую статистику.
    Нужно частично отсортировать массив по убыванию и взять первые k элмента.

    Или просто сделать массив k максимумов и итеративно добавлять?
    '''
    with open('day_1.txt', 'r') as fd:
        lines = fd.read().splitlines()
    elves = []
    cur = 0
    for line in lines:
        if line == '':
            elves.append(cur)
            cur = 0
        else:
            # аааааа!!!! короче, надо сортировать по убыванию
            # сделаем такой изящный костыль
            cur -= int(line)
    elves.append(cur)
    part_sort(elves, 3)
    print(-sum(elves[0:3]))


part_2()
