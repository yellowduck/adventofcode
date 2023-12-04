"""
--- Day 3: Gear Ratios ---

https://adventofcode.com/2023/day/3

In my original version, I extracted the symbols into
their own data structure. this is completely unnecessary
because the info already exists in the input data.

The input data consists of an array of lines,
where each line is a string (because str in Python are
accessible in the same way as list - so no need to convert)

We could avoid the edge detection (<0, >max) by appending
to the data. Use "." on all edges.

Use of a yield funtion to allow termination of a nested
loop which was created when up/down/left/right searching
was combined. Use of product to create the x/y co-ords/
"""
import re
from collections import defaultdict
from itertools import product


def problem(part=1, input=None):
    if not input:
        data = open("day3.input", "rt").read().split()
    else:
        data = input.split("\n")

    digits = re.compile(r"(\d+)")

    class Lookup:
        def __init__(self, lookupTable) -> None:
            self._data = lookupTable
            self._max_rows = len(lookupTable)-1
            self._max_cols = len(lookupTable[0])-1
        def check_for_data(self, r,c):
            # out of bounds check
            if (r<0 or r>self._max_rows or
                c<0 or c>self._max_cols):
                return False
            else:
                return not(self._data[r][c].isdigit() or self._data[r][c] == ".")


    # now search for numbers
    sum_of_parts = 0
    lookup = Lookup(data)
    found_gears = defaultdict(list)

    def look_around(row, c_start, c_end):
        neighbours = [-1, 0, 1]
        for col in range(c_start, c_end):
            for r_offset, c_offset in product(neighbours, neighbours):
                yield row+r_offset, col+c_offset

    for row,line in enumerate(data):
        for number in digits.finditer(line):
            ratio = int(number.group(0))

            for r, c in look_around(row, number.start(), number.end()):
                if lookup.check_for_data(r, c):
                    # print(f"detected: {int(number.group(0))}")
                    found_gears[f"{r}_{c}"].append(ratio)
                    sum_of_parts += ratio
                    break

    sum_of_gears = 0
    for gearList in found_gears.values():
        if len(gearList)==2:
            sum_of_gears += gearList[0]*gearList[1]

    return sum_of_parts, sum_of_gears

if __name__ == '__main__':


    # extra tests
    testList = [
        # right of symbol
        ("...*617...", 617),
        # right of symbol
        ("527*...", 527),
        # look up
        (".620......\n.....*....", 0),
        ("..621.....\n.....*....", 621),
        ("...622....\n.....*....", 622),
        ("....623...\n.....*....", 623),
        (".....624..\n.....*....", 624),
        ("......625.\n.....*....", 625),
        (".......626\n.....*....", 0),
        # look down
        (".....*....\n.530......", 0),
        (".....*....\n..531.....", 531),
        (".....*....\n...532....", 532),
        (".....*....\n....533...", 533),
        (".....*....\n.....534..", 534),
        (".....*....\n......535.", 535),
        (".....*....\n.......536", 0),

    ]

    for test,expected in testList:
        parts,_ = problem(1, test)
        assert parts==expected, f"{parts=} : {expected=}"

    test="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    parts, gears = problem(1, test)
    assert parts==4361
    assert gears==467835


    parts, gears = problem(1)
    print(f"Part 1: {parts=}")
    assert parts==533784

    print(f"Part 2: {gears=}")
    assert gears==78826761
