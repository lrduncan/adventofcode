import os
import unittest

def part1(filename):
    total = 0

    with open(os.getcwd()+filename, "r+") as file1:
        while True:
            line = file1.readline()
            if not line:
                break
            # print(line)
            line_split = [int(x) for x in line.split(" ")]

            if is_safe_report(line_split):
                total += 1

    return total

def part2(filename):
    total = 0

    with open(os.getcwd()+filename, "r+") as file1:
        while True:
            line = file1.readline()
            if not line:
                break
            # print(line)
            line_split = [int(x) for x in line.split(" ")]

            if is_safe_report(line_split):
                total += 1
            else:
                for i in range(len(line_split)):
                    a = line_split.copy()
                    del a[i]
                    if is_safe_report(a):
                        total += 1
                        break

    return total

def is_safe_report(arr):
    if are_all_valid_differences(arr):
        if are_all_decreasing(arr) or are_all_increasing(arr):
            return True

def are_all_increasing(arr):
    prev = arr[0]
    for x in arr[1:]:
        if not is_increasing(prev, x):
            return False
        prev = x
    return True

def are_all_decreasing(arr):
    prev = arr[0]
    for x in arr[1:]:
        if not is_decreasing(prev, x):
            return False
        prev = x
    return True

def are_all_valid_differences(arr):
    prev = arr[0]
    for x in arr[1:]:
        if not check_difference(prev, x):
            return False
        prev = x
    return True

def is_increasing(first, second):
    return first < second

def is_decreasing(first, second):
    return first > second

def check_difference(first, second):
    return 1 <= abs(first-second) <= 3

class Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1("/example.txt"), 2)
    def test_part2(self):
        self.assertEqual(part2("/example.txt"), 4)

if __name__ == "__main__":
    # unittest.main()
    print("Part 1 Example answer is " + str(part1("/example.txt")))

    print("Part 1 answer is " + str(part1("/input.txt")))

    print("Part 2 Example answer is " + str(part2("/example.txt")))

    print("Part 2 answer is " + str(part2("/input.txt")))
