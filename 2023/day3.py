"""
--- Day 3: Gear Ratios ---

https://adventofcode.com/2023/day/3
"""
from collections import defaultdict
import re

def problem(part=1, input=None):
    if not input:
        data = open("day3.input", "rt").read().split()
    else:
        data = input.split("\n")

    digits = re.compile(r"(\d+)")

    # parse twice; once for parts symbols, then for adjacent numbers
    # store symbols in an array same size as data for easy lookup

    numCols = len(data[0])
    numRows = len(data)
    symbolLookup = []

    # extract non-alpha chars
    symbols = set()
    for line in data:
        colLookup = [None]*numCols
        for col, char in enumerate(line):
            if not char.isdigit() and not char==".":
                symbols.add(char)
                colLookup[col] = char
        symbolLookup.append(colLookup)
    print(f"{symbols=}")

    class Lookup:
        def __init__(self, lookupTable) -> None:
            self._data = lookupTable
            self._max_rows = len(lookupTable)-1
            self._max_cols = len(lookupTable[0])-1
        def check_for_data(self, r,c):
            if (r<0 or r>self._max_rows or
                c<0 or c>self._max_cols):
                return False
            else:
                return self._data[r][c] is not None

    # now search for numbers
    sum_of_parts = 0
    lookup = Lookup(symbolLookup)
    found_gears = defaultdict(list)

    for row,line in enumerate(data):
        for number in digits.finditer(line):
            ratio = int(number.group(0))
            # print(f"detected: {int(number.group(0))}")
            # brute force
            # LOOK LEFT
            if lookup.check_for_data(row, number.end()):
                found_gears[f"{row}_{number.end()}"].append(ratio)
                sum_of_parts += ratio
                # print(f"matched left: {row},{number.end()} : {ratio}")
            # look right
            if lookup.check_for_data(row, number.start()-1):
                found_gears[f"{row}_{number.start()-1}"].append(ratio)
                sum_of_parts += ratio
                # print(f"matched right: {row},{number.start()-1} : {ratio}")

            # look up
            for col in range(number.start()-1,number.end()+1):
                if lookup.check_for_data(row-1, col):
                    found_gears[f"{row-1}_{col}"].append(ratio)
                    sum_of_parts += ratio
                    # print(f"matched up: {row-1},{col} : {ratio}")
                    break

            # look down
            for col in range(number.start()-1,number.end()+1):
                if lookup.check_for_data(row+1, col):
                    found_gears[f"{row+1}_{col}"].append(ratio)
                    sum_of_parts += ratio
                    # print(f"matched down: {row+1},{col} : {ratio}")
                    break

    sum_of_gears = 0
    for gearList in found_gears.values():
        if len(gearList)==2:
            sum_of_gears += gearList[0]*gearList[1]

    pass



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

    # for test,exp in testList:
    #     parts,_problem(1, test)
    #     assert parts==exp

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
