import os
import unittest

def part1(filename):
    total = 0
    puzzle = []

    with open(os.getcwd()+filename, "r+") as file1:
        while True:
            line = file1.readline()
            if not line:
                break
            # print(line)
            puzzle.append([x for x in line.strip()])

    try:
        for i, l in enumerate(puzzle):
            for j, v in enumerate(l):
                    # must check if there is an X to start always
                    if puzzle[i][j] == 'X':
                        # ->
                            if check(puzzle, i+1, j, 'M'):
                                if check(puzzle, i+2, j, 'A'):
                                    if check(puzzle, i+3, j, 'S'):
                                        total += 1
                        # <-
                            if check(puzzle, i-1, j, 'M'):
                                if check(puzzle, i-2, j, 'A'):
                                    if check(puzzle, i-3, j, 'S'):
                                        total += 1
                        # ^
                            if check(puzzle, i, j-1, 'M'):
                                if check(puzzle, i, j-2, 'A'):
                                    if check(puzzle, i, j-3, 'S'):
                                        total += 1
                        # \/
                            if check(puzzle, i, j+1, 'M'):
                                if check(puzzle, i, j+2, 'A'):
                                    if check(puzzle, i, j+3, 'S'):
                                        total += 1
                        # upper left
                            if check(puzzle, i-1, j-1, 'M'):
                                if check(puzzle, i-2, j-2, 'A'):
                                    if check(puzzle, i-3, j-3, 'S'):
                                        total += 1
                        # upper right
                            if check(puzzle, i+1, j-1, 'M'):
                                if check(puzzle, i+2, j-2, 'A'):
                                    if check(puzzle, i+3, j-3, 'S'):
                                        total += 1
                        # lower right
                            if check(puzzle, i+1, j+1, 'M'):
                                if check(puzzle, i+2, j+2, 'A'):
                                    if check(puzzle, i+3, j+3, 'S'):
                                        total += 1
                        # lower left
                            if check(puzzle, i-1, j+1, 'M'):
                                if check(puzzle, i-2, j+2, 'A'):
                                    if check(puzzle, i-3, j+3, 'S'):
                                        total += 1
    except IndexError:
        pass

    return total

def part2(filename):
    total = 0
    puzzle = []

    with open(os.getcwd()+filename, "r+") as file1:
        while True:
            line = file1.readline()
            if not line:
                break
            # print(line)
            puzzle.append([x for x in line.strip()])

    try:
        for i, l in enumerate(puzzle):
            for j, v in enumerate(l):
                    # must check if there is an A to start always
                    if puzzle[i][j] == 'A':
                        # MM
                        # SS
                        if check(puzzle, i-1, j-1, 'M'):
                            if check(puzzle, i-1, j+1, 'M'):
                                if check(puzzle, i+1, j-1, 'S'):
                                    if check(puzzle, i+1, j+1, 'S'):
                                        total += 1
                        # SS
                        # MM
                        if check(puzzle, i-1, j-1, 'S'):
                            if check(puzzle, i-1, j+1, 'S'):
                                if check(puzzle, i+1, j-1, 'M'):
                                    if check(puzzle, i+1, j+1, 'M'):
                                        total += 1
                        # MS
                        # MS
                        if check(puzzle, i-1, j-1, 'M'):
                            if check(puzzle, i-1, j+1, 'S'):
                                if check(puzzle, i+1, j-1, 'M'):
                                    if check(puzzle, i+1, j+1, 'S'):
                                        total += 1
                        # SM
                        # SM
                        if check(puzzle, i-1, j-1, 'S'):
                            if check(puzzle, i-1, j+1, 'M'):
                                if check(puzzle, i+1, j-1, 'S'):
                                    if check(puzzle, i+1, j+1, 'M'):
                                        total += 1
    except IndexError:
        pass

    return total

def check(puzzle, i, j, letter):
    if i < 0 or j < 0:
        return False
    try:
        return puzzle[i][j] == letter
    except IndexError:
        return False

class Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(part1("/example.txt"), 18)
    def test_part2(self):
        self.assertEqual(part2("/example2.txt"), 9)

if __name__ == "__main__":
    # unittest.main()
    print("Part 1 Example answer is " + str(part1("/example.txt")))

    print("Part 1 answer is " + str(part1("/input.txt")))

    print("Part 2 Example answer is " + str(part2("/example.txt")))

    print("Part 2 answer is " + str(part2("/input.txt")))
