import os
from heapq import heapify, heappush, heappop 

def part1(filename):
    total = 0
    l, r = [], []
    heapify(l)
    heapify(r)

    with open(os.getcwd()+filename, "r+") as file1:
        while True:
            line = file1.readline()
            if not line:
                break
            # print(line)
            line_split = line.split("   ")
            heappush(l, int(line_split[0]))
            heappush(r, int(line_split[1]))
        
    while l:
        left = heappop(l)
        right = heappop(r)
        val = abs(left-right)
        total += val
    return total

def part2(filename):
    ans = 0
    with open(os.getcwd()+filename, "r+") as file1:
        l, r = [], {}
        while True:
            line = file1.readline()
            if not line:
                break
            # print(line)
            line_split = line.strip().split("   ")
            # make hash table of right to find occurrences then go through the left list and multiply
            l.append(int(line_split[0]))
            r[int(line_split[1])] = r.get(int(line_split[1]), 0) + 1
        for n in l:
            ans += n * r.get(n, 0)
        return ans


if __name__ == "__main__":
    print("Part 1 Example answer is " + str(part1("/example1.txt")))

    print("Part 1 answer is " + str(part1("/input1.txt")))

    print("Part 2 Example answer is " + str(part2("/example1.txt")))

    print("Part 2 answer is " + str(part2("/input1.txt")))
