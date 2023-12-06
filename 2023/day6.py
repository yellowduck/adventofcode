"""
--- Day 6: Wait For It ---

https://adventofcode.com/2023/day/6
"""
import re
import math

def problem(part=1, test=None):

    data = test.split("\n")
    digits = re.compile(r"\d+")

    times = digits.findall(data[0])
    distances = digits.findall(data[1])

    if part==1:
        times = list(map(int, times))
        distances = list(map(int, distances))

    if part==2:
        times = [int("".join(times))]
        distances = [int("".join(distances))]

    # without optimisation: real 0m5.918s

    winners = []
    for time, distance in zip(times, distances):
        # >>> [a * (n-a) for a in range(1,n)]
        # [6, 10, 12, 12, 10, 6]
        win = 0
        for press in range(1,time):
            td = press*(time-press)
            win += (td > distance)
        winners.append(win)

    return math.prod(winners)

if __name__ == '__main__':

    test="""Time:      7  15   30
    Distance:  9  40  200"""

    day6="""Time:        55     82     64     90
    Distance:   246   1441   1012   1111"""

    exp = 288
    result = problem(part=1, test=test)
    assert exp==result, f"Part 1: received={result} {exp=}"

    exp = 608902
    result = problem(part=1, test=day6)
    print(f"Part 1: {result}")
    assert exp==result, f"Part 1: received={result} {exp=}"

    exp = 71503
    result = problem(part=2, test=test)
    assert exp==result, f"Part 2: received={result} {exp=}"

    exp = 46173809
    result = problem(part=2, test=day6)
    print(f"Part 2: {result}")
    assert exp==result, f"Part 2: received={result} {exp=}"
