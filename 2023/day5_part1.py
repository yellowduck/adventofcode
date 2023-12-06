"""
--- Day 5: If You Give A Seed A Fertilizer ---

https://adventofcode.com/2023/day/5
"""
from collections import defaultdict

def problem(part=1, test=False):
    if not test:
        data = open("day5.input", "rt").readlines()
    else:
        data = test.split("\n")

# map ranges
# destination-range-start source-range-start range-length
# 50 98 2 -> 50,51 98,99 which means 98 maps to 01 & 99 -> 51
# unmapped numbers map to same value 10 -> 10

    # first line is seed list
    seeds = list(map(int, data[0].split(" ")[1:]))
    mappings = defaultdict(list)
    order = {}

    for line in data:
        line = line.strip()

    get_line = iter(data[1:])

    for line in get_line:
        line = line.strip()
        if line.endswith("map:"):
            mapping = line.split(" ")[0]
            # will terminate on empty string
            source,_,destination = mapping.split("-")
            order[source] = destination
            while line := next(get_line, "").strip():
                # store ranges in a list on the mapping
                dest_start, source_start, range_length = map(int,line.split(" "))
                mappings[mapping].append([range(dest_start,dest_start+range_length),range(source_start,source_start+range_length)])

    lowest = []

    def get_seed(seeds, part=1):
        if part==1:
            for seed in seeds:
                yield seed
        else:
            #! this does not work - the values and ranges are too large
            for start, length in zip(seeds[0::2], seeds[1::2]):
                for seed in range(start, start+length):
                    yield seed


    for seed in get_seed(seeds, part):
        source = "seed"
        number = seed
        while source in order.keys():
            mapping = f"{source}-to-{order[source]}"
            for dest_range, source_range in mappings[mapping]:
                if number in source_range:
                    number = dest_range[source_range.index(number)]
                    break
            source = order[source]

        lowest.append(number)

    return min(lowest)

if __name__ == '__main__':

    test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    exp_lowest = 35
    lowest = problem(part=1, test=test)
    assert exp_lowest==lowest, f"Part 1: received={lowest} {exp_lowest=}"

    exp_lowest = 324724204
    lowest = problem(part=1)
    print(f"Part 1: {lowest}")
    assert exp_lowest==lowest, f"Part 1: received={lowest} {exp_lowest=}"

    exp_lowest = 46
    lowest = problem(part=2, test=test)
    assert exp_lowest==lowest, f"Part 2: received={lowest} {exp_lowest=}"

    # lowest = problem(part=2)
    # print(f"Part 2: {lowest}")
    # assert exp_lowest==lowest, f"Part 2: received={lowest} {exp_lowest=}"
