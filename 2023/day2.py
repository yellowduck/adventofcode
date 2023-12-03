"""
--- Day 2: Cube Conundrum ---

https://adventofcode.com/2023/day/2
"""

from collections import defaultdict
import math
import re

def problem(part=1, input=None):
    if not input:
        data = open("day2.input", "rt")
    else:
        data = input.split("\n")

    gamePattern = re.compile(r"Game\s+(\d+)")

    games = defaultdict(list)

    for line in data:
        line = line.strip()
        gameStr, cubeStr = line.split(":")
        gameId = int(gamePattern.match(gameStr).groups()[0])

        # [' 3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green']
        for gameSet in cubeStr.split(";"):

            # ['', '3', 'blue', '4', 'red']
            colours = gameSet.replace(",","").split(" ")
            games[gameId].append({colour:int(n) for colour,n in zip(colours[2::2],colours[1::2])})

    # keep original parse in case needed for pt2
    # and reduce cube counts into a single dict for easier processing
    gamesCombined = {}
    for gameId, gameSet in games.items():
        colours = {'red': 0, 'green': 0, 'blue': 0}
        for colourCount in gameSet:
            for colour, cubes in colourCount.items():
                colours.update({colour: max(cubes, colours.get(colour, 0))})

        gamesCombined[gameId] = colours



    maxColours ={"red":12, "green":13, "blue":14}
    sum_of_ids = 0
    power = 0
    for gameId, colourCount in gamesCombined.items():
        # if any(n==0 for n in colourCount.values()):
        #     print(f"Zero found for {gameId=} ...skipping")
        #     continue
        if all(n<=maxColours[c] for c,n in colourCount.items()):
            # print(f"{gameId=}:{colourCount=}")
            sum_of_ids += gameId
        # Part II
        power += math.prod(colourCount.values())

    if part==1:
        return sum_of_ids
    else:
        return power

if __name__ == '__main__':

    test="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    assert problem(1, test)==8

    print(f"Part 1: {problem(1)}")
    # 2409 is too high - data still had \n on end of lines!
    assert problem(1)==2265

    assert problem(2, test)==2286

    print(f"Part 2: {problem(2)}")
    assert problem(2)==64097
