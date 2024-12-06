import os
import unittest
import re

def part1(filename):
    total = 0

    with open(os.getcwd()+filename, "r+") as file1:
        while True:
            line = file1.readline()
            if not line:
                break
            # print(line)
            muls = re.findall(r'mul\((\d+,\d+)\)', line)
            for x in muls:
                nums = [int(y) for y in x.split(",")]
                total += nums[0] * nums[1]

    return total

def part2(filename):
    total = 0

    with open(os.getcwd()+filename, "r+") as file1:
        mul_enabled = True
        while True:
            line = file1.readline()
            if not line:
                break
            # print(line)
            muls = re.findall(r'mul\((\d+,\d+)\)|(do\(\))|(don\'t\(\))', line)
            # print(muls)

            for x, y, z in muls:
                if y:
                    mul_enabled = True
                elif z:
                    mul_enabled = False
                elif mul_enabled:
                    nums = [int(n) for n in x.split(",")]
                    total += nums[0] * nums[1]

    return total



class Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1("/example.txt"), 161)
    def test_part2(self):
        self.assertEqual(part2("/example2.txt"), 48)

if __name__ == "__main__":
    # unittest.main()
    print("Part 1 Example answer is " + str(part1("/example.txt")))

    print("Part 1 answer is " + str(part1("/input.txt")))

    print("Part 2 Example answer is " + str(part2("/example2.txt")))

    print("Part 2 answer is " + str(part2("/input.txt")))
